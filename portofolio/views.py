from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import PostForm

from .models import post
# Create your views here.

def Home(request):
    posts = post.objects.filter(active=True, featured=True)[0:3]

    context = {'Posts' :posts}
    return render(request, 'base/index.html',  context)

def Posts(request):
    posts = post.objects.filter(active=True)

    context ={'Posts':posts}
    return render(request, 'base/posts.html', context)

def Post(request, pk):
    post = post.objects.get(id=pk)

    context = {'post': post}
    return render(request, 'base/post.html', context)

def Profile(request):
    return render(request, 'base/profile.html')
    

#crud views

@login_required (login_url='home')
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()        
        return redirect('posts')

    context = {'form':form}
    return render(request, 'base/post_form.html', context)

 
@login_required(login_url='home')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostFrom(instance=post)

    if request.method =='POST':
        form = PostFrom(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('Posts')

    context = {'form': form}
    return render(request, 'base/post_form.html', context)

@login_required(login_url='home')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post')
    context = {"item :post"}
    return render(request, 'base/delete.html' ,context)