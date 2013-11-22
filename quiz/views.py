from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response
from quiz.models import Question, Answer, Result


def quiz(request, errors=None, answers=None, name=''):
	questions = Question.objects.all()
	print answers
	return render_to_response("quiz.html", {'questions':questions, 'errors':errors, 'chosen_answers':answers, 'name':name}, RequestContext(request))
		

def results(request):
	errors = {}
	if request.method == "GET":
		return redirect("/quiz/")
	else:
		try:
			name = request.POST['name']
			if len(name) < 3:
				errors['no_name'] = "That's too short to be your name.  Don't be a jerk."
			if name == None or name == '':
				errors['no_name'] = "This is literally the easiest question on the page."
			questions_objects = Question.objects.all()		
			questions = [{'question' : question, 
						  'user_answer' : Answer.objects.get(pk=request.POST[str(question.pk)])} for question in questions_objects]
			score=0
			for question in questions:
				if question['user_answer'].correct:
					score += 1
			# for question in questions:
			# 	user_answers[question] = Answer.objects.get(pk=question.pk).text
			score_percentage = int(round(float(score) * 100 / len(questions)))
			print "Score {0}, # of questions: {1}, Percent: {2}".format(score, len(questions), score_percentage)
			if score_percentage >= 80:
				score_message = "Great job!  Looks you know Paul and Jason pretty well!  Or you cheated."
			elif score_percentage >= 60:
				score_message = "Not bad, but you could do better.  Maybe spend some more time with the boys.  Perhaps take them out to a fancy dinner.  Your treat."
			else:
				score_message = "Wow.  Have you ever even met Paul and Jason?  Or did you just let a blind monkey take the quiz for you?"
			name = request.POST['name']
			if name == '':
				errors['no_name'] = "This is literally the easiest question on the page."
			r = Result(name=name, score=score_percentage)
			r.save()
			
		except KeyError:
			errors['empty_question'] = True
		if errors:
			question_keys = [str(question.pk) for question in Question.objects.all()]
			answers = [int(request.POST[key]) for key in question_keys if request.POST.get(key) != None]
			return quiz(request, errors=errors, answers=answers, name=name)
		else:
			return render_to_response("results.html", 
				{'score' : score, 
				 'score_percentage' : score_percentage,
				 'score_message' : score_message,
				 'questions' : questions,
				 # 'user_answers' : user_answers,
				 }, 
				 RequestContext(request))


def high_scores(request):
	scores = Result.objects.order_by('-score')
	return render_to_response('high_scores.html', 
			{'scores' : scores}, 
			RequestContext(request))