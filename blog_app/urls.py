from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog-list' ),
    path('write/', views.CreateBlog.as_view(), name='create-blog' ), #Use 'write/' as path
    path('details/<int:pk>', views.blog_details, name='blog-details' ),
]