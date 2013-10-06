from django.contrib import admin
from models import Message

class MessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'message', 'response', 'date')

admin.site.register(Message, MessageAdmin)