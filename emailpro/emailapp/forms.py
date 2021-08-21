from django import forms
from django.contrib.auth.models import User

class EmailForm(forms.Form):
	name = forms.CharField()
	remarks = forms.CharField(widget = forms.Textarea)
	