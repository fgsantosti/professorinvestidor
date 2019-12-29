from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

from .forms import PostForm
from django.utils import timezone

# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def view_index(request):
	#me = User.objects.get(username='celso')
	#posts = Post.objects.filter(author=me)
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, pk):
	#post = Post.objects.filter(pk=id_post)
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	form = PostForm()
	post = form.save(commit=False)
	post.author = request.user
	post.published_date = timezone.now()
	post.save()
	return render(request, 'blog/post_edit.html', {'form': form})

def form_na_mao(request):
	title = request.POST['title']
	texto = request.POST['text']
	Post.objects.create(author='fgs', title=title, text=texto)
