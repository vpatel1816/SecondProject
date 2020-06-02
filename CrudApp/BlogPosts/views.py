from django.shortcuts import render
from .models import Blogs

# Create your views here.
def home(request):
	blog = Blogs.objects.all
	return render(request,'BlogPosts/home.html', {'blog':blog})