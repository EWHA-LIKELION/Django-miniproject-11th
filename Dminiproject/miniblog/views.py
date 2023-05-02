from django.shortcuts import render,get_object_or_404,redirect
from .models import Main
from django.utils import timezone

# Create your views here.

def main(request):
    main_list=Main.objects.order_by('-uploaddate')    #작성일시 역순으로 정렬
    context={'mains':main_list}
    return render(request,'main.html',context)

def detail(request, main_id):
    main_detail=get_object_or_404(Main,pk=main_id)
    return render(request,'detail.html',{'kk':main_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_main=Main()
    new_main.title=request.POST['title']
    new_main.uploaddate=timezone.now()
    new_main.username=request.POST['username']    #왜 여기서 안되는 걸까요...
    new_main.content=request.POST['content']
    new_main.save()
    return redirect('main')

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
    main_update.save()
    return redirect('main')

#우에헤헤
