from django.urls import path
from . import views

app_name = 'blog_login'

urlpatterns = [
    path('signup/',views.sign_up, name='signup'),
    path('login/',views.sign_in, name='signin'),
    path('signout/',views.sign_out, name='signout'),
    path('profile/',views.profile, name='profile'),
    path('edit-profile/',views.EditProfile, name='edit-profile'),
    path('password/',views.password_change, name='change-password'), #Path should be 'password/' when you use PasswordChangeForm class
    
]