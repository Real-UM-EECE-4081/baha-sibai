from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})
