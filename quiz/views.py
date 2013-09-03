from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response
from quiz.models import Question, Answer, User

def quiz(request):
	if request.method == "GET":
		questions = Question.objects.all()		
	return render_to_response("quiz.html", {'questions':questions}, RequestContext(request))
		

def results(request):
	if request.method == "GET":
		return redirect("/quiz/")
	else:
		questions = Question.objects.all()		
		user_answers = {}
		score=0
		print len(questions)
		for question_num in range(1, len(questions)+1):
			if Answer.objects.get(pk=request.POST[str(question_num)]).correct:
				score += 1
			user_answers[question_num] = Answer.objects.get(pk=request.POST[str(question_num)]).text
		print user_answers
		score_percentage = int(float(score) * 100 / len(questions))
		if score_percentage >= 80:
			score_message = "Great job!  Looks you know Paul and Jason pretty well!  Or you cheated."
		elif score_percentage >= 60:
			score_message = "Not bad, but you could do better.  Maybe spend some more time with the boys.  Perhaps take them out to a fancy dinner.  Your treat."
		else:
			score_message = "Wow.  Have you ever even met Paul and Jason?  Or did you just let a blind monkey take the quiz for you?"
		print(request.POST)	
		return render_to_response("results.html", 
			{'score' : score, 
			 'score_percentage' : score_percentage,
			 'score_message' : score_message,
			 'questions' : questions,
			 'user_answers' : user_answers,
			 }, 
			 RequestContext(request))