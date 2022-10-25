from django.contrib import admin
from django.urls import path, include
from django.conf import settings   #import this to use pics in the project
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns     #import this to use pics in the project
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('blog_login.urls')),
    path('blog/',include('blog_app.urls')),
    path('', views.index, name='index')
]

urlpatterns += staticfiles_urlpatterns()   #These settings should be added foe static files to work
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #These settings should be added foe static files to work
