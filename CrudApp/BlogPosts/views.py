from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Blogs

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogsSerializsers

# Create your views here.
def home(request):
	blog = Blogs.objects.all
	return render(request,'BlogPosts/home.html', {'blog':blog})

def random(request):
	data = {1:{'name':'vishal','age':20},1 :{'name':'vishal','age':20}}
	return JsonResponse(data)

class Blogss(APIView):
	def get(self, request):
		values = Blogs.objects.all()
		Serializer = BlogsSerializsers(values, many=True)
		return Response(Serializer.data)


def edit(request, id):
	blogs = Blogs.objects.get(id=id)
	return render(request,'BlogPosts/edit.html', {'blogs':blogs})

def deletee(request, id):
	blog = Blogs.objects.get(id=id)
	blog.delete()
	return redirect('/')

def update(request, id):
	if request.method == 'POST':
		blogs = Blogs.objects.get(id=id)
		blogs.blog_title = request.POST.get('blog_title')
		blogs.blog = request.POST.get('blog')
		blogs.save()
		return redirect('/')

	else:
		return redirect('/')

def add(request):
	if request.method == 'POST':
		blog_title 	= request.POST.get('blog_title')
		blog 		= request.POST.get('blog')
		blog_author = request.POST.get('blog_author')
		new_blog = Blogs(blog_title=blog_title, blog=blog, blog_author=blog_author)
		new_blog.save()
		return redirect('/')

	else:
		return render(request, 'BlogPosts/add.html')