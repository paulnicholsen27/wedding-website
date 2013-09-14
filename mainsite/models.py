from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=256)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name