from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import results
# Create your views here.
def index(request):
    result = results.objects.all()
    return render(request,"index.html",{'result':result})
def add(request):
    if request.method == 'POST':
        user_title = request.POST['user_title']
        user_description = request.POST['user_description']
        user_link = request.POST['user_link']
        user_image = request.POST['user_image']
        user_result = results.objects.create(title = user_title,paragraph =user_description,link =user_link,image=user_image)
        user_result.save()
        return redirect('index')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name taken!!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password, email = email, first_name= first_name,last_name = last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Password didn\'t match!!!')
            return redirect('register')
        return redirect('/')
    else:
        return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'User not found!!!')
            return redirect('/')
    else:
        return redirect('/')
def logout(request):
    auth.logout(request)
    return redirect('/')