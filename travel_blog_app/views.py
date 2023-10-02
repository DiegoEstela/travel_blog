from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, r'travel_blog_app/base.html')

def index(request):
    posts = Post.objects.all()
    return render(request, r'travel_blog_app/index.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, r'travel_blog_app/new_post.html', {'form': form})
