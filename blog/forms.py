from django import forms 
from .models import Photo, User

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('file', )

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model = Post 
# 		fields = ('title',)


class UserForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = '__all__'

		