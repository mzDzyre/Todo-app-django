from django.shortcuts import render,redirect
from .models import *
from datetime import datetime,date

def dashboard(request):
    queryset = Todo.objects.filter(is_active=True).order_by('date')
    context = {'todo_list':queryset}
    return render(request, 'todos/dashboard.html',context)

def add_todo(request):
    if request.method == 'POST':
        data = request.POST
        date = data.get('date')
        task = data.get('task')
        
        Todo.objects.create(
            task=task, date=date
        )
        return redirect('/')
    return render(request, 'todos/dashboard.html')

def update_check(request, id):
    data = Todo.objects.get(id=id)
    if data.status == True:
        data.status = False
    elif data.status == False:
        data.status = True
    data.updated_at = datetime.now()
    data.save()
    return redirect('/')

def update_todo(request, id):
    queryset = Todo.objects.get(id=id)
    formatted_date = queryset.date.strftime("%Y-%m-%d")
    if request.method == 'POST':
        data = request.POST
        date = data.get('date')
        task = data.get('task')
        print("Getted Data", date, "and", task)
        queryset.date = date
        queryset.task = task
        queryset.updated_at = datetime.now()
        queryset.save()
        return redirect('/')
    context={'taskUpdate':queryset,'formatted_date': formatted_date} 
    return render(request,'todos/update.html', context)

def delete_todo(request,id):
    queryset = Todo.objects.get(id=id)
    queryset.is_active = False
    queryset.save()
    return redirect("/")

def today_todo(request):
    queryset = Todo.objects.filter(date=date.today(),is_active=True)
    context={'todo_list':queryset, 'today_date':date.today()} 
    return render(request, 'todos/dashboard.html',context)
