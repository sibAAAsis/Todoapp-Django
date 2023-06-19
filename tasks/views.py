#This the views of the app
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Max
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def account(request):
    user = request.user
    return render(request, 'account.html', {'user': user})

@login_required
def toggle_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')
    else:
        return redirect('task_list')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def create_task(request):
 if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
 else :  
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Save the form data without committing to the database yet
            task.user = request.user  # Assign the currently logged-in user as the task owner
            task.save()  # Commit the task to the database
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'confirm_delete_task.html', {'task': task})




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or perform additional actions
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after successful update
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})