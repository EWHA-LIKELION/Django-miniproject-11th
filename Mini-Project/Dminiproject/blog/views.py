from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Comment, HashTag
from django.utils import timezone
from .forms import Blogform, CommentForm
# Create your views here.
#superuser - jieun3977/rlawldms828!
#테스트 user - silver/rlawldms828! 

def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    blog_hashtag=blog_detail.hashtag.all()
    return render(request,'detail.html',{'blog':blog_detail, 'hashtags':blog_hashtag})

def new(request):
    form=Blogform()
    return render(request,'new.html',{'form':form})

def create(request):
    form=Blogform(request.POST, request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.date=timezone.now()
        new_blog.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_blog.hashtag.add(new_hashtag[0])
        return redirect('detail',new_blog.id)
    return redirect('home')

def delete(reqeust,blog_id):
    blog_delete=get_object_or_404(Blog,pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request,blog_id):
    blog_update=get_object_or_404(Blog,pk=blog_id)
    return render(request,'update.html',{'blog':blog_update})

def update(request,blog_id):
    blog_update=get_object_or_404(Blog,pk=blog_id)
    blog_update.type=request.POST['type']
    blog_update.title=request.POST['title']
    blog_update.body=request.POST['body']
    #blog_update.hashtag=request.POST['hashtags']
    blog_update.save()
    return redirect('detail',blog_id)

def add_comment(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail',blog_id)
        
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form':form})

def comment_detail(request, comment_id): #댓글 업데이트 페이지 이동
    comment_detail=get_object_or_404(Comment,pk=comment_id)
    post_ID=comment_detail.post
    return render(request,'update_comment.html',{'comment':comment_detail,'blog':post_ID})

def update_comment(request, blog_id, comment_id): #댓글 업데이트 저장
    #원래 하려했던 아래 함수로 다시 함수 설정하고 url에서 업데이트 페이지 가는거 하나, 업데이트 완료하는거 하나 url 총 두개 만들어야함
    #url에서 하나는 comment_id만 받고 다른 하나는 comment_id와 blog_id 둘 다 받기
    comment_update=get_object_or_404(Comment,pk=comment_id)
    comment_post=get_object_or_404(Blog,pk=blog_id)
    comment_update.username=request.POST['username']
    comment_update.comment_text=request.POST['comment_text']
    comment_update.post=comment_post
    comment_update.save()
    return redirect('detail',blog_id)
    #my_comment=Comment.objects.get(id=comment_id)
    #comment_form=CommentForm(instance=my_comment)
    #if request.method == "POST":
    #    update_form = CommentForm(request.POST, instance=my_comment)
    #    if update_form.is_valid():
    #        update_form.save()
    #        return redirect('detail', blog_id)
    #return render(request, 'update_comment.html',{'comment_form':comment_form})