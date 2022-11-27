from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog-list' ),
    path('write/', views.CreateBlog.as_view(), name='create-blog' ), #Use 'write/' as path
    path('details/<int:pk>', views.blog_details, name='blog-details' ),
    path('liked/<pk>', views.liked, name='liked-post' ),
    path('unliked/<pk>/', views.unliked, name='unliked-post' ),
    path('my-blog/', views.MyBlog.as_view(), name='my-blog' ),
    path('edit-blog/<pk>', views.UpdateBlog.as_view(), name='edit-blog' ),
]