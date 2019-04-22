from django.urls import path
from . import views

urlpatterns = [
	path('basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
	path('user-upload/', views.user_upload, name='user_upload'),
]