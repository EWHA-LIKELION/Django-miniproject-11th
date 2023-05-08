from django.shortcuts import render,get_object_or_404,redirect
from .models import Posting
from .forms import Blogform
from django.utils import timezone

# Create your views here.

def home(request):
    #posts=Posting.objects     #Blog데이터들을 객체형태로 blogs변수에 넣어줌
    #return render(request,'home.html',{'blogs':blogs})
    return render(request,'home.html')


def detail(request, post_id):
    post_detail=get_object_or_404(Posting,pk=post_id)
    return render(request,'detail.html',{'post':post_detail})

def week(request, pk):
    print(pk)
    if(pk==1): posts=Posting.objects.filter(category__icontains="월")
    elif(pk==2): posts=Posting.objects.filter(category__icontains="화")
    elif(pk==3): posts=Posting.objects.filter(category__icontains="수")
    elif(pk==4): posts=Posting.objects.filter(category__icontains="목")
    elif(pk==5): posts=Posting.objects.filter(category__icontains="금")
    elif(pk==6): posts=Posting.objects.filter(category__icontains="토")
    elif(pk==7): posts=Posting.objects.filter(category__icontains="일")
    return render(request,'week.html',{'posts':posts})

def new(request): #이동하는 함수
    return render (request,'new.html')

def create(request): #저장
    form=Blogform(request.POST,request.FILES)
    if form.is_valid(): #유효성 검사
        new_blog=form.save(commit=False)
        new_blog.date=timezone.now()
        new_blog.save()
        return redirect ('detail',new_blog.id)
    return redirect('home')
	# post=Posting()
    # new_post.title=request.POST['title']
    # new_post.body=request.POST['body']
    # new_post.date=timezone.now()
    # new_post.category=request.POST['category']
    # new_post.image = request.FILES['image']
    # new_post.save()
    # return redirect('home')


def delete(request, post_id):
    blog_delete=get_object_or_404(Posting,pk=post_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request,post_id): #페이지 이동
    post_update=get_object_or_404(Posting,pk=post_id)
    return render(request,'update.html',{'blog':post_update})

def update(request,post_id): #수정
    print(request)
    blog_update=get_object_or_404(Posting,pk=post_id)
    blog_update.title=request.POST['title']
    blog_update.body=request.POST['body']
    blog_update.date=timezone.now()
    blog_update.category=request.POST['category']
    #blog_update.image = request.FILES['image']
    blog_update.save()
    return redirect('home')

