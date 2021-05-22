from django import forms
from .models import Contact
from django.db import models
from django import forms

# class CheckForm(forms.ModelForm):
#     date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     class Meta:
#         model = Check
#         fields = ('date', 'country',)

# class BookForm(forms.ModelForm):
#     date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     class Meta:
#         model = Book
#         fields = ('Name', 'date', 'country','Contact')
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('Name', 'Email','Subject', 'Message',)