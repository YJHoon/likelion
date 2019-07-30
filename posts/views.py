from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def hobby(request):
    return render(request, 'posts/climbing.html')

def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        time = request.POST.get('time')
        ingredient = request.POST.get('ingredient')
        category = request.POST.get('category')
        level = request.POST.get('level')
        post = Post.objects.create(title=title, content=content, image=image, time=time, ingredient=ingredient, category=category, level=level)
        return redirect('home')
    return render(request, 'posts/new.html')

def edit(request, id):
    posts = get_object_or_404(Post, pk=id)  
    return render(request, 'posts/edit.html', {'posts':posts})

def update(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=id)  
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        time = request.POST.get('time')
        ingredient = request.POST.get('ingredient')
        category = request.POST.get('category')
        level = request.POST.get('level')
        
        post.title = title
        post.content = content
        post.time = time
        post.image = image
        post.ingredient = ingredient
        post.category = category
        post.level = level
        post.save()
        return redirect('posts:show', post.pk)
  
def show(request, id):
    posts = get_object_or_404(Post, pk=id)  
    default_view_count = posts.view_count
    posts.view_count = default_view_count + 1
    posts.save()
    return render(request, 'posts/show.html', {'posts':posts})

def delete(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=id)  
        post.delete()
        return redirect('home')
