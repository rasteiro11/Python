from django.urls import path
from . import views

urlpatterns = [
	path("<int:id>", views.index, name="index"),
	#path("<str:name>", views.index, name="index"),

]