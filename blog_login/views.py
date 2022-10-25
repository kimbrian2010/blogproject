from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from blog_login.forms import SignUpForm, UserEditProfile, ProfilePic

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST': 
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            
    dict = {'form':form, 'registered':registered}        
    return render(request, 'blog_login/signup.html', context=dict)
        
        
def sign_in(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'blog_login/login.html', context={'form':form})


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog_login:signin'))


@login_required
def profile(request):
    return render(request, 'blog_login/profile.html', context={})


@login_required
def EditProfile(request):
    current_user = request.user
    form = UserEditProfile(instance=current_user)
    if request.method == 'POST':
        form = UserEditProfile(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserEditProfile(instance=current_user)   #Saving current user data after editing
    return render(request, 'blog_login/edit_profile.html', context={'form':form})


@login_required
def password_change(request):
    current_user = request.user
    password_changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            password_changed = True
        form = PasswordChangeForm(current_user, data=request.POST) #current password is saved in variable 'data' since old password will needed in the update form
    return render(request, 'blog_login/password_change.html', context={'form':form, 'password_changed':password_changed})


@login_required 
def add_profile_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES) #Pass the image file uploaded in the form ie 'request.FILES'
        if form.is_valid():
            user_obj = form.save(commit=False) #Don't save data as yet
            user_obj.user = request.user # assign user object to current user(logged in user)
            user_obj.save() #Save data
            return HttpResponseRedirect(reverse('blog_login:profile')) # Return to Profile page upon adding picture
    return render(request, 'blog_login/add_profile_pic.html',context={'form':form})


@login_required
def change_profile_pic(request):  # pip install 'django_cleanup' to be replacing old profile pics with new ones
    form = ProfilePic(instance=request.user.user_profile)  #Accessing existing pic using 'user_profile' related name
    if request.method=='POST':
        form =  ProfilePic(request.POST, request.FILES, instance=request.user.user_profile) # pass current profile pic
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_login:profile'))
    return render(request, 'blog_login/add_profile_pic.html', context={'form':form})