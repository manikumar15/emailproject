from django.shortcuts import render
from .import forms
from django.core.mail import send_mail

# Create your views here.

def email_view(request):
	form = forms.EmailForm()
	if request.method=="POST":
		form = forms.EmailForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			remarks = form.cleaned_data['remarks']
			send_mail("New Enquiry",name,remarks,["manikumaredepalli@gmail.com"], fail_silently = False)
	return render(request,"mail.html",{'form':form})
















