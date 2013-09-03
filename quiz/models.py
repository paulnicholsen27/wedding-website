from django.db import models

# Create your models here.

class Question(models.Model):
	text = models.CharField(max_length=256)
	result_message = models.CharField(max_length=256, null=True, blank=True)

	def __unicode__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	text =	models.CharField(max_length=256)
	correct = models.BooleanField()

	def __unicode__(self):
		return self.text

class User(models.Model):
	name = models.CharField(max_length=256)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name