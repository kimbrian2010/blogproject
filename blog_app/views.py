from django.shortcuts import render, HttpResponseRedirect

from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from blog_app.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid 


# Create your views here.

#def blog_list(request):
    #return render(request, 'blog_app/blog_list.html', context={})


class BlogList(ListView):
    context_object_name = 'blogs' #passing context in class based view
    model = Blog
    template_name = 'blog_app/blog_list.html' 
    queryset = Blog.objects.order_by('-publish_date') #Display articles by new to old


class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_app/create_blog.html'
    fields = ('blog_title', 'blog_content','blog_image')
    
    def form_valid(self, form):
        blog_obj = form.save(commit = False)
        blog_obj.author = self.request.user #assigning current user to author of created user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-")+ "-" + str(uuid.uuid4()) #replacing spaces in the title with "-"
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))
    
    
def blog_details(request, pk):
    blog = Blog.objects.get(pk=pk)
        
    return render(request, 'blog_app/blog_details.html', context={'blog':blog})