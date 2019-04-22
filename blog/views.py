from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.core.files.storage import FileSystemStorage
from .models import Photo
from .forms import PhotoForm, UserForm


class BasicUploadView(View):
	def get(self, request):
		photos_list = Photo.objects.all()

		return render(self.request, 'home.html', {'photos': photos_list})

	def post(self, request):
		form = PhotoForm(self.request.POST, self.request.FILES)

		if form.is_valid():
			photo = form.save()
			photos= Photo.objects.all()
			photo_html = render_to_string('includes/photo_list.html', {'photos':photos})
			data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url,'photo_html':photo_html}
		else:
			data = {'is_valid': False}

		return JsonResponse(data)

def user_upload(request):
	form = UserForm()
	if request.method=='POST' and request.FILES['photo']:
		form = UserForm(request.POST, request.FILES)
		
		if form.is_valid():
			user = form.save()

		return render(request,'user_upload.html',{'form':form,'user_photo_url':user.photo.url})

	return render(request,'user_upload.html',{'form':form})
	