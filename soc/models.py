from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class post(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length = 100)
	text = models.CharField(max_length = 1000)
	time=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title


class createpost(ModelForm):
	class Meta:
		model=post
		fields = ['title','text']


class comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
	post = models.ForeignKey(post, on_delete=models.SET_NULL, null=True, blank= True)
	time=models.DateTimeField(auto_now=True)
	text = models.CharField(max_length=1000)


class childcomment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
	parent = models.ForeignKey(comment, on_delete=models.SET_NULL, null=True, blank= True)
	time=models.DateTimeField(auto_now=True)
	text = models.CharField(max_length=1000)	


class writecomment(ModelForm):
	class Meta:
		model=comment
		fields = ['text']

