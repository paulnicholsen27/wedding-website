from django.db import models
from django.contrib import admin

class Image(models.Model):
	title = models.CharField(max_length=150, blank=True, null=True)
	image = models.FileField(upload_to="images/")
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.image.name

class ImageAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["__unicode__", "title"]

admin.site.register(Image, ImageAdmin)