from django.forms import ModelForm, TextInput, Textarea, Select

from News.models import NewsModel


class AddNewsForm(ModelForm):
    class Meta:
        model = NewsModel
        exclude = ['author']


class UpdateNewsForm(ModelForm):
    class Meta:
        model = NewsModel
        exclude = ['author', 'date']
        widgets = {
            'header': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'type': Select(attrs={'class': 'form-control', 'placeholder': 'Тип'}),
        }