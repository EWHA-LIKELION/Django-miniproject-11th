from django.shortcuts import render, get_object_or_404, redirect
from .models import Ddabong, HashTag, Comment
from django.utils import timezone
from .forms import Ddabongform, CommentForm

# Create your views here.

def home(request):
    ddabongs = Ddabong.objects
    return render(request, 'home.html', {'ddabongs':ddabongs})

def detail(request, ddabong_id):
    ddabong_detail = get_object_or_404(Ddabong, pk=ddabong_id)
    ddabong_hashtag = ddabong_detail.hashtag.all()
    return render(request, 'detail.html', {'ddabong': ddabong_detail, 'hashtags': ddabong_hashtag})

def new(request):
    form = Ddabongform()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = Ddabongform(request.POST, request.FILES)
    if form.is_valid():
        new_ddabong = form.save(commit=False)
        new_ddabong.date = timezone.now()
        new_ddabong.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_ddabong.hashtag.add(new_hashtag[0])
        return redirect('detail', new_ddabong.id)
    return redirect('home')

def delete(request, ddabong_id):
    ddabong_delete = get_object_or_404(Ddabong,pk=ddabong_id)
    ddabong_delete.delete()
    return redirect('home')

def update_page(request, ddabong_id):
    ddabong_update = get_object_or_404(Ddabong, pk=ddabong_id)
    return render(request, 'update.html', {'ddabong':ddabong_update})

def update(request, ddabong_id):
    ddabong_update = get_object_or_404(Ddabong, pk=ddabong_id)
    ddabong_update.title=request.POST['title']
    ddabong_update.body=request.POST['body']
    ddabong_update.save()
    return redirect('home')

def add_comment(request, ddabong_id):
    ddabong = get_object_or_404(Ddabong, pk=ddabong_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = ddabong
            comment.save()
            return redirect('detail', ddabong_id)

    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form' : form}
    )

