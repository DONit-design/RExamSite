from django import forms
from django.forms import TextInput, Textarea, Select

from Exams.models import ExamModel


class ExamCreateForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        exclude = ['date', 'author']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя экзамена...'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание экзамена...'}),
            'subject': Select(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Имя экзамена:',
            'description': 'Описание экзамена:',
            'subject': 'Предмет:'
        }
