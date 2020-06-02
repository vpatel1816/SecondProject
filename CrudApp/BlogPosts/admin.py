from django.contrib import admin
from .models import Blogs
# Register your models here.

class Blogss(admin.ModelAdmin):
	list_display = ('blog_title','blog_author','blog_date')


admin.site.register(Blogs, Blogss)