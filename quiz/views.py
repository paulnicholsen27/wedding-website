from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response
from quiz.models import Question, Answer, Result


def quiz(request, errors=None, answers=None, name=''):
	questions = Question.objects.all()
	print answers
	return render_to_response("quiz.html", {'questions':questions, 'errors':errors, 'chosen_answers':answers, 'name':name}, RequestContext(request))
		

def results(request):
	errors = {'test':'test'}
	if request.method == "GET":
		return redirect("/quiz/")
	else:
		try:
			questions_objects = Question.objects.all()		
			questions = [{'question' : question, 
						  'user_answer' : Answer.objects.get(pk=request.POST[str(question.pk)])} for question in questions_objects]
			score=0
			for question in questions:
				if question['user_answer'].correct:
					score += 1
			# for question in questions:
			# 	user_answers[question] = Answer.objects.get(pk=question.pk).text
			score_percentage = int(float(score) * 100 / len(questions))
			if score_percentage >= 80:
				score_message = "Great job!  Looks you know Paul and Jason pretty well!  Or you cheated."
			elif score_percentage >= 60:
				score_message = "Not bad, but you could do better.  Maybe spend some more time with the boys.  Perhaps take them out to a fancy dinner.  Your treat."
			else:
				score_message = "Wow.  Have you ever even met Paul and Jason?  Or did you just let a blind monkey take the quiz for you?"
			name = request.POST.get('name')
			r = Result(name=name, score=score_percentage)
			r.save()
			return render_to_response("results.html", 
				{'score' : score, 
				 'score_percentage' : score_percentage,
				 'score_message' : score_message,
				 'questions' : questions,
				 # 'user_answers' : user_answers,
				 }, 
				 RequestContext(request))
		except KeyError:
			question_keys = [str(question.pk) for question in Question.objects.all()]
			answers = [int(request.POST[key]) for key in question_keys if request.POST.get(key) != None]
			if len(question_keys) != len(answers):
				errors['empty_question'] = "Make sure you've answered all the questions! (Hint: You didn't.)"
			name = request.POST.get('name', None)
			if not name:
				errors['no_name'] = "This is literally the easiest question on the page."
			return quiz(request, errors=errors, answers=answers, name=name)


def high_scores(request):
	scores = Result.objects.order_by('-score')
	return render_to_response('high_scores.html', 
			{'scores' : scores}, 
			RequestContext(request))