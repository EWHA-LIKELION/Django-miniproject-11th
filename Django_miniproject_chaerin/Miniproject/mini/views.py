from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.utils import timezone
from django.db.models import Q

# Create your views here.

def home(request):
    #posts=Posting.objects     #Post데이터들을 객체형태로 posts변수에 넣어줌
    #return render(request,'home.html',{'posts':posts})
    return render(request,'home.html')


def detail(request, post_id):
    post_detail=get_object_or_404(Posting,pk=post_id)
    post_hashtag=post_detail.hashtag.all()
    return render(request,'detail.html',{'post':post_detail,'hashtags':post_hashtag})

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
    form=Postform(request.POST,request.FILES)
    if form.is_valid(): #유효성 검사
        new_post=form.save(commit=False)
        new_post.date=timezone.now()
        new_post.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(",")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_post.hashtag.add(new_hashtag[0])
        return redirect ('detail',new_post.id)
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
    post_delete=get_object_or_404(Posting,pk=post_id)
    post_delete.delete()
    # image = self.find_own_image(image_id)
    # if image is None:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    # image.delete()
    return redirect('home')

def update_page(request,post_id): #페이지 이동
    post_update=get_object_or_404(Posting,pk=post_id)
    return render(request,'update.html',{'post':post_update})

def update(request,post_id): #수정
    print(request)
    post_update=get_object_or_404(Posting,pk=post_id)
    post_update.title=request.POST['title']
    post_update.body=request.POST['body']
    post_update.date=timezone.now()
    post_update.category=request.POST['category']
    #post_update.image = request.FILES['image']
    post_update.save()
    return redirect('home')


def add_comment(request,post_id):
    post=get_object_or_404(Posting,pk=post_id)

    if request.method == 'POST':
        form = Commentform(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('detail',post_id)
        
    else:
        form = Commentform()

    return render(request,'add_comment.html',{'form':form})


def update_comment_page(request,comment_id):
    comment_update=get_object_or_404(Comment,pk=comment_id)
    post_ID=comment_update.post
    return render(request,'update_comment.html',{'post':post_ID,'comment':comment_update})

def update_comment(request,post_id,comment_id): #수정
    print(request)
    comment_update=get_object_or_404(Comment,pk=comment_id)
    comment_update.username=request.POST['username']
    comment_update.comment_text=request.POST['comment_text']
    comment_update.created_at=timezone.now()
    comment_update.post=get_object_or_404(Posting,pk=post_id)
    #post_update.image = request.FILES['image']
    comment_update.save()
    return redirect('detail',post_id)

def delete_comment(request,post_id, comment_id):
    comment_delete=get_object_or_404(Comment,pk=comment_id)
    comment_delete.delete()
    return redirect('detail',post_id)

def search(request):
    search=request.GET.get('search','')
    postf=Posting.objects.filter(        #제목 또는 내용에 search가 있는것 필터링 #2
     Q(title__icontains = search) | Q(body__icontains = search)
    )
    return render(request, 'search.html',{'postf':postf}) 
