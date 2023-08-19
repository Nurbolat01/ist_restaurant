from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Category, Photo, Post


def menu(requests):
	categories = Category.objects.prefetch_related(
		Prefetch('photo_set', queryset=Photo.objects.order_by('name'), to_attr='items')).all()
	# items_by_category = {category: Photo.objects.filter(category=category)}
	context = {'categories':categories}
	return render(requests,'menu.html', context)
# Create your views here.

def home(requests):

	return render(requests, 'index.html')


def about(requests):

	return render(requests, 'about.html')


def post(requests):
	posts = Post.objects.all()
	context = {'posts':posts}
	return render(requests, 'blog.html', context)


def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	context = {'post': post}
	return render(request, 'blog-single.html', context)


