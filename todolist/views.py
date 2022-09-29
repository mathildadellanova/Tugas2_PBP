from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def index(request):
    task_list = Task.objects.filter(user=request.user)
    context = {'task_list': task_list, 'username': request.user.username}
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:index")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login')
def create_task(request):
    if request.method == 'POST':
        # buat task baru
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task(
                title=form.cleaned_data['title'], description=form.cleaned_data['description'], user=request.user, date=datetime.date.today())
            new_task.save()
            messages.success(request, 'Added one task')
            return redirect('todolist:index')
    form = TaskForm()
    context = {'form': form}
    return render(request, 'create-task.html', context)

def update(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)

    if (task.is_finished):
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()

    return HttpResponseRedirect(reverse("todolist:index"))

def delete(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)

    task.delete()

    return HttpResponseRedirect(reverse("todolist:index"))