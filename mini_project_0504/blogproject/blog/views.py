from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import Blogform, Commentform

# Create your views here.

def home(request):
    blogs=Blog.objects 
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)

    comment_form = Commentform()

    return render(request,'detail.html',{'blog':blog_detail, 'comment_form':comment_form})

def new(request):
    form=Blogform()
    return render(request, 'new.html', {'form':form})

def create(request):
    form =Blogform(request.POST, request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.date=timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

def delete(request, blog_id):
    blog_delete=get_object_or_404(Blog,pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request, blog_id):
    blog_update = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'update.html',{'blog':blog_update})

def update(request, blog_id):
    blog_update = get_object_or_404(Blog,pk=blog_id)
    blog_update.title=request.POST['title']
    blog_update.body=request.POST['body']
    blog_update.save()
    return redirect('home')

def create_comment(request, blog_id):
    filled_form = Commentform(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog,pk=blog_id)
        finished_form.save()
    return redirect('detail', blog_id)