from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task

# fetching data from database







def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')  #return all task which is not completed and with decending order
    
    completed_tasks = Task.objects.filter(is_completed = True) #return all task which is completed
    

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'home.html', context)