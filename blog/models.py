from django.db import models
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify


class Photo(models.Model):
	title = models.CharField(max_length=255, blank=True)
	file = models.FileField(upload_to='photos/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
# 	post = models.ForeignKey(to="Post", related_name='photos',on_delete=models.CASCADE)

# class Post(models.Model):
# 	title = models.CharField(max_length=100)


class User(models.Model):
	name = models.CharField(max_length=109)
	photo = models.ImageField(upload_to="users/")

	def __str__(self):
		return self.name