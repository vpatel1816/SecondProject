from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('add', views.add, name= 'add'),
    path("edit/<int:id>", views.edit, name='edit'),
    path("delete/<int:id>", views.deletee),
    path("update/<int:id>", views.update),
]
