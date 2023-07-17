from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from .forms import TodoForm
from .models import Todo


def home(request):
    """homepage with home.html"""
    return render(request, 'todo/home.html')


def signupuser(request):
    """in this view we give form for sign up(REGISTRATINS) for new users and check password users with signupuser.html"""

    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'That username has already taken. Choose new name.'})
        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Password did not match!'})


def loginuser(request):
    """in this view we give form for login for users and authentication with loginuser.html"""

    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html',
                          {'form': AuthenticationForm, 'error': 'Username and password did not match!'})
        else:
            login(request, user)
            return redirect('currenttodos')


# @login_required
def logoutuser(request):
    """in this view we logout users and redirects to home page"""
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def createtodo(request):
    """in this view create new task(todo) with validation form with createtodo.html"""

    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm})
    else:
        try:
            form = TodoForm(request.POST)
            if form.is_valid():
                newtodo = form.save(commit=False)
                newtodo.user = request.user
                newtodo.save()
                return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error': 'Bad data passed in'})


@login_required
def edittodo(request, todo_pk):
    """in this view we take our task from db and edit task and
    if without change we stay in page edit, but if we change entry we redirect to list with
    currents tasks(current.html)"""

    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'GET':
        return render(request, 'todo/edittodo.html', {'form': TodoForm(instance=todo)})
    else:
        try:
            form = TodoForm(instance=todo, data=request.POST)
            if form.is_valid():
                newtodo = form.save(commit=False)
                newtodo.user = request.user
                newtodo.save()
                return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/currenttodos.html', {'form': TodoForm(), 'error': 'Bad info'})


@login_required
def currenttodos(request):
    """here we take from db out currents tasks with redis cache"""
    todos_cache = cache.get('todos_cache')
    if not todos_cache:
        todos_cache = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
        cache.set('todos_cache', todos_cache, 10)
    else:
        todos_cache = cache.get('todos_cache')
    return render(request, 'todo/currenttodos.html', {'todos_cache': todos_cache})


@login_required
def viewtodo(request, todo_id):
    """here we with help -get_object_or_404- take todo or give exception
    bound with current user"""
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo/viewtodo.html', {'todo': todo})


@login_required
def completetodo(request, todo_pk):
    """here we take list with complited tasks if model - Todo.datecompleted(null=True), will be False
     we send this task in complited tasks"""
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    """we delete our task from db"""

    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')


@login_required
def completedtodos(request):
    """we take only tasks where datecompleted__isnull is False(complited tasks) with redis cache"""

    completed_todos_cache = cache.get('completed_todos_cache')
    if not completed_todos_cache:
        completed_todos_cache = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by(
            '-datecompleted')
        cache.set('completed_todos_cache', completed_todos_cache, 10)
    else:
        completed_todos_cache = cache.get('completed_todos_cache')
    return render(request, 'todo/completedtodos.html', {'completed_todos_cache': completed_todos_cache})
