from django.shortcuts import render
from .models import Task
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main/register.html', context)

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')