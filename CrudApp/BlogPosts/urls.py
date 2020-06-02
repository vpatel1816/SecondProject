from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('add', views.add, name= 'add'),
    path("edit/<int:id>", views.edit),
    path("delete/<int>/id", views.deletee),
]
