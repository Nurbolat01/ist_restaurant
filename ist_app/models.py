from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.name


class Photo(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	image = models.ImageField(null=False, blank=False)
	name = models.CharField(max_length=150, null=False, blank=False)
	description = models.TextField()
	compound = models.CharField(max_length=100, null=True, blank=True)
	price = models.IntegerField(null=False)




	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title