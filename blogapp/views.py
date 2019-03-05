from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'blogs/blog.html',{'blogs' : blogs, 'posts' :posts })

def detail(request, blog_id):
    blogs_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blogs_detail})

def new(request):
    return render(request, 'blogs/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))