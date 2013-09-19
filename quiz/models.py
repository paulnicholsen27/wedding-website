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


class Result(models.Model):
	name = models.CharField(max_length=256)
	date_taken = models.DateField(auto_now_add=True)
	score = models.IntegerField()
