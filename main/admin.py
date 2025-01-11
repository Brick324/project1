from django.contrib import admin
from .models import Quiz, Question, Answer
from users.models import CustomUser
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CustomUser)