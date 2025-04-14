from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/posts_page.html', {'post': post})

@login_required(login_url="/users/login")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatPost(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:list')
    else:    
        form = forms.CreatPost()
    return render(request, 'posts/post_new.html', {'form': form})