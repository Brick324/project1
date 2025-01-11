from django.forms import ModelForm
from .models import Result

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['quiz', 'score']