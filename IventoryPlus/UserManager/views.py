from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login ,logout
from django.contrib import messages
from .models import Profile
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect('Product:product_list')  
        else:
             messages.error(request, 'Invalid Credentials')
    

    
    return render(request, 'UserManager/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('UserManager:login')
        except:
            return HttpResponse('User already exists')
    
    return render(request, 'UserManager/signup.html')



def logout_view(request):
    logout(request)
    return redirect('UserManager:login')


def profile(request):
    user_profile = Profile.objects.get(user=request.user)# get the profile of the logged in user
    return render(request, 'UserManager/profile.html',{'user_profile':user_profile})


def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_profile.bio = request.POST['bio']
        user_profile.age = request.POST['age']
        user_profile.address = request.POST['address']
        user_profile.phone = request.POST['phone']
        user_profile.image = request.FILES.get('image')
        user_profile.save()
        return redirect('UserManager:profile')
    return render(request, 'UserManager/edit_profile.html',{'user_profile':user_profile})