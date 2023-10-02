from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Post
from .forms import PostForm , AuthorForm , CategoryForm

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

def search_post(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        results = []
    return render(request, r'travel_blog_app/search_post.html', {'results': results, 'query': query})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AuthorForm()
    return render(request, r'travel_blog_app/create_author.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # O la URL a la que quieras redirigir
    else:
        form = CategoryForm()
    return render(request, r'travel_blog_app/create_category.html', {'form': form})