from django.urls import path
from . import views

urlpatterns=[
	path('menu/', views.menu, name='menu'),
	path('about/', views.about, name='about'),
	path('posts/', views.post, name='posts'),
	path('post/<int:pk>', views.post_detail, name='post'),
	path('', views.home, name='home'),
]