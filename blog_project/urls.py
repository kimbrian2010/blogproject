from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('blog_login.urls')),
    path('blog/',include('blog_app.urls')),
    path('', views.index, name='index')
]
