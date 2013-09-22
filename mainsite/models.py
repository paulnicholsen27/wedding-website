from django.db import models
from django.forms import ModelForm

class User(models.Model):
	name = models.CharField(max_length=256)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Message(models.Model):
	name = models.CharField(max_length=256)
	message = models.TextField()
	response = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	