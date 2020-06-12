from django.db import models

# Create your models here.
class Blogs(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_author = models.CharField(max_length=10)
	blog_date = models.DateTimeField(('created'), auto_now_add=True, db_index=True, null=True)
	blog = models.TextField(max_length=500)

	def __str__(self):
		return self.blog_title

