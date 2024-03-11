from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from datetime import date,datetime
from django.contrib.auth.models import auth

@login_required
def main(request):
    tasks = Task.objects.filter(user=request.user)
    
    today = date.today()
    for task in tasks:
        days_remaining = (task.date - today).days
        task.days_remaining = days_remaining
    
    return render(request, 'main.html', {'tasks': tasks})

@login_required
def completed(request):
    tasks = Task.objects.filter(user=request.user, status='Completed')
    
    today = date.today()
    for task in tasks:
        days_remaining = (task.date - today).days
        task.days_remaining = days_remaining
    
    return render(request, 'main.html', {'tasks': tasks})

@login_required
def pending(request):
    tasks = Task.objects.filter(user=request.user, status='Pending')
    
    today = date.today()
    for task in tasks:
        days_remaining = (task.date - today).days
        task.days_remaining = days_remaining
    
    return render(request, 'main.html', {'tasks': tasks})

@login_required
def newtask(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
        remind = request.POST.get('remind')
        priority = request.POST.get('priority')
        
        user = request.user

        task = Task.objects.create(user=user, name=name, desc=desc, date=date, remind=remind, priority=priority, status='Pending')
        return redirect('main')
   
    else:
        return render(request, 'newtask.html')
    
def update_or_delete_entry(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        entry_id = request.POST.get('entry_id')
        
        if action == 'complete':
            entry = Task.objects.get(id=entry_id)
            entry.status = 'Completed'
            entry.save()
            print('status updated')
            
        elif action == 'delete':
            Task.objects.filter(id=entry_id).delete()
            print('status deleted')
        
        return redirect('main')
    
    else:
        return redirect('main')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
