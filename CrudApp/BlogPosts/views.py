from django.shortcuts import render, redirect
from .models import Blogs

# Create your views here.
def home(request):
	blog = Blogs.objects.all
	return render(request,'BlogPosts/home.html', {'blog':blog})

def edit(request, id):
	blogs = Blogs.objects.get(id=id)
	return render(request,'BlogPosts/edit.html', {'blogs':blogs})

def deletee(request, id):
	blog = Blogs.objects.get(id=id)
	blog.delete()
	return redirect('/')

def update(request, id):
	if request.method == 'POST':
		updates = Blogs.objects.get(id=id)
		blog_title  = request.POST.get('blog_title')
		blog        = request.POST.get('blog')
		blog_author = request.POST.get('blog_author') 
		updates = Blogs(blog_title=blog_title, blog=blog, blog_author=blog_author)
		updates.save()
		return redirect('/')

	else:
		return redirect('www.google.com')


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