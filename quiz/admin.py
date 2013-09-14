from django.contrib import admin
from quiz.models import Question, Answer

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('text', 'question', 'correct')

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'score')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
