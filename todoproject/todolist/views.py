from django.shortcuts import render, get_object_or_404
from .models import Todo, Category
from .forms import TodoForm, CategoryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'todolist/index.html')

def todos(request):
    todo_list=Todo.objects.all()
    return render(request, 'todolist/todos.html',{'todo_list':todo_list})

def category(request, id):
    cat_egory= get_object_or_404(Todo.objects, id=id)
    return render(request, 'todolist/category.html', {'cat_egory':cat_egory})

@login_required
def newtodo(request):
    form=TodoForm
    if request.method== 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TodoForm()

    else:
        form=TodoForm()
    return render(request, 'todolist/newtodos.html', {'form': form})

#@login_required
def newcategory(request):
    form=CategoryForm
    if request.method== 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            post=cform.save(commit=True)
            post.save()
            form=CategoryForm()

    else:
        form=CategoryForm()
    return render(request, 'todolist/newcategory.html', {'form': form})

def loginmessage(request):
    return render(request, 'todolist/login.html')

def logoutmessage(request):
    return render(request, 'todolist/logout.html' )