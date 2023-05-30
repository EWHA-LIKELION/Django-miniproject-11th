from django.shortcuts import render,get_object_or_404,redirect
from .models import Main, HashTag
from django.utils import timezone
from .forms import Mainform,CommentForm

# Create your views here.
#WNTJRDLAL
#dsfd

def main(request):
    main_list=Main.objects.order_by('-uploaddate')    #작성일시 역순으로 정렬
    context={'mains':main_list}
    return render(request,'main.html',context)

def detail(request, main_id):
    main_detail=get_object_or_404(Main,pk=main_id)
    main_hashtag=main_detail.hashtag.all()
    return render(request,'detail.html',{'kk':main_detail, 'hashtags':main_hashtag})

def new(request):
    form=Mainform()
    return render(request, 'new.html',{'form':form})

def create(request):
    form=Mainform(request.POST, request.FILES)
    if form.is_valid():
        new_main=form.save(commit=False)
        new_main.uploaddate=timezone.now()
        new_main.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_main.hashtag.add(new_hashtag[0])
        return redirect('detail',new_main.id)
    return redirect('main')

    ''' form 사용 전
    new_main=Main()
    new_main.title=request.POST['title']
    new_main.uploaddate=timezone.now()
    new_main.username=request.POST['username']    #왜 여기서 안되는 걸까요...
    new_main.content=request.POST['content']
    new_main.save()
    return redirect('main')
    '''


def delete(request, main_id):
    main_delete=get_object_or_404(Main,pk=main_id)
    main_delete.delete()
    return redirect('main')


def update_page(request,main_id):
    main_updates=get_object_or_404(Main,pk=main_id)
    return render(request,'update.html',{'upup':main_updates})

def update(request,main_id):
    main_update=get_object_or_404(Main,pk=main_id)
    main_update.title=request.POST['title']
    main_update.username=request.POST['username']
    main_update.content=request.POST['content']
    main_update.uploaddate=timezone.now()
    main_update.save()
    return redirect('main')

def add_comment(request,main_id):
    main=get_object_or_404(Main,pk=main_id)

    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=main
            comment.save()
            return redirect('detail',main_id)
        
    else :
        form=CommentForm()
    
    return render(request,'add_comment.html',{'form':form})

# git 다시 pr