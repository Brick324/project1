from django.db import models
from users.models import CustomUser

# Create your models here.

class Quiz(models.Model):
  name = models.CharField(max_length=300)


class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)


class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)
  is_correct = models.BooleanField(default=False)

class Result(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  score = models.IntegerField()

  class Meta:
    ordering = ['-score']
    unique_together = ('user', 'quiz')

  def __str__(self):
    return f"{self.user.username} - {self.quiz}: {self.score}"