from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Count
from .models import Quiz, Question, Answer, Result
from django.core.paginator import Paginator
from typing import Optional

def index(request):
    return render(request, "main/index.html")

def vehicles(request):
    return render(request, "main/vehicles.html")

def car(request):
    return render(request, "main/car.html")

def carbody(request):
    return render(request, "main/cardetails/carbody.html")

def electrical(request):
    return render(request, "main/cardetails/electrical.html")

def engine(request):
    return render(request, "main/cardetails/engine.html")

def transmission(request):
    return render(request, "main/cardetails/transmission.html")


def plane(request):
    return render(request, "main/plane.html")

def fuselage(request):
    return render(request, "main/planedetails/fuselage.html")

def landinggear(request):
    return render(request, "main/planedetails/landinggear.html")

def tail(request):
    return render(request, "main/planedetails/tail.html")

def turbine(request):
    return render(request, "main/planedetails/turbine.html")

def wing(request):
    return render(request, "main/planedetails/wing.html")


def train(request):
    return render(request, "main/train.html")

def trainbody(request):
    return render(request, "main/traindetails/trainbody.html")

def roof(request):
    return render(request, "main/traindetails/roof.html")

def electrobox(request):
    return render(request, "main/traindetails/electrobox.html")






def register(request):
    return render(request, "user/templates/registration.html")

def login(request):
    return render(request, "user/templates/login.html")

def start_quiz_view(request) -> HttpResponse:
  topics = Quiz.objects.all().annotate(questions_count=Count('question'))
  
  if request.user.is_authenticated:
    results = Result.objects.filter(user=request.user).select_related('quiz')
    results_dict = {result.quiz_id: result.score for result in results}
  else:
    results_dict = {}

  return render(
    request, 'main/start.html', context={'topics': topics, 'results_dict': results_dict}
  )


def get_questions(request, is_start=False) -> HttpResponse:
  if is_start:
    request = _reset_quiz(request)
    question = _get_first_question(request)
  else:
    question = _get_subsequent_question(request)
    if question is None:
      return get_finish(request)

  answers = Answer.objects.filter(question=question)
  request.session['question_id'] = question.id  # Update session state with current question id.

  return render(request, 'main/partials/question.html', context={
    'question': question, 'answers': answers
  })


def _get_first_question(request) -> Question:
  quiz_id = request.POST['quiz_id']
  return Question.objects.filter(quiz_id=quiz_id).order_by('id').first()


def _get_subsequent_question(request) -> Optional[Question]:
  quiz_id = request.POST['quiz_id']
  previous_question_id = request.session['question_id']

  try:
    return Question.objects.filter(
      quiz_id=quiz_id, id__gt=previous_question_id
    ).order_by('id').first()
  except Question.DoesNotExist:  # I.e., there are no more questions.
    return None


def get_answer(request) -> HttpResponse:
  submitted_answer_id = request.POST['answer_id']
  submitted_answer = Answer.objects.get(id=submitted_answer_id)

  if submitted_answer.is_correct:
    correct_answer = submitted_answer
    request.session['score'] = request.session.get('score', 0) + 1
  else:
    correct_answer = Answer.objects.get(
      question_id=submitted_answer.question_id, is_correct=True
    )

  return render(
    request, 'main/partials/answer.html', context={
      'submitted_answer': submitted_answer,
      'answer': correct_answer,
    }
  )


def get_finish(request) -> HttpResponse:
  quiz = Question.objects.get(id=request.session['question_id']).quiz
  questions_count = Question.objects.filter(quiz=quiz).count()
  score = request.session.get('score', 0)
  percent = int(score / questions_count * 100)
  request = _reset_quiz(request)
  result, created = Result.objects.update_or_create(
    user = request.user,
    quiz = quiz,
    defaults={'score': max(score, Result.objects.filter(user=request.user, quiz=quiz).first().score if Result.objects.filter(user=request.user, quiz=quiz).exists() else 0)}

  )

  return render(request, 'main/partials/finish.html', context={
    'questions_count': questions_count, 'score': score, 'percent_score': percent
  })


def _reset_quiz(request) -> HttpRequest:
  """
  We reset the quiz state to allow the user to start another quiz.
  """
  if 'question_id' in request.session:
    del request.session['question_id']
  if 'score' in request.session:
    del request.session['score']
  return request


# Create your views here.
