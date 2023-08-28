import django.forms
from django import forms
from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title','description','image','prise','auction']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control form-control-lg'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control form-control-lg'}),
            'prise' : forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}),
            'auction' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'image' : forms.FileInput(attrs={'class' : 'form-comtrol form-comtrol-lg'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака')
        return title