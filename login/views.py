from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("main")
        
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")
                
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup')
            
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup')
            
        else:
            user= User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('new user created')
            return redirect('login')
        
    else:
        return render(request, 'signup.html')
    
def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            # Replace these credentials with your Mailgun SMTP credentials
            mailgun_username = config('MAILGUN_USER')
            mailgun_password = config('MAILGUN_PASS')

            try:
                send_mail(
                    'Message from Contact Form',  # Subject
                    message,  # Message body
                    'postmaster@mg.tasks.fun',  # Sender's email address
                    ['ogdevelopers6@gmail.com'],  # Recipient's email address (replace with your own)
                    fail_silently=False,
                    auth_user=mailgun_username,
                    auth_password=mailgun_password,
                    connection=None,
                )
                return redirect('/')
            except Exception as e:
                return HttpResponse(f'Failed to send email. Error: {str(e)}')