from django.conf import settings #I'm importing the settings file so i can reference the emails i saved there. 
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm, SignUpForm
# If you want to use querysets you have to import the model that you want to query. 
from .models import SignUp 


# Create your views here.
def home(request):
	active_user = str(request.user)
	context = {
		"active_user": active_user, 
	}
	
	return render(request, "home.html", context)


def contact(request):
	title="Great to have you on board!"
	text_center=True
	form = ContactForm(request.POST or None)
	# now, we cant save this because it is not a model form. 
	if form.is_valid():
	# 	for key, value in form.cleaned_data.items(): #items() python3 <--> iteritems() python2
	# 		print(key, value)
	# 		#print(form.cleaned_data.get(key))

		form_email= form.cleaned_data.get('email')
		form_message=form.cleaned_data.get('message')
		form_full_name=form.cleaned_data.get('full_name')
		# print(email, message, full_name)
		subject="Site contact form"
		from_email=settings.EMAIL_HOST_USER
		to_email = [from_email, 'philipp_rathjen@hotmail.de']
		contact_message= "%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)


		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context = {
		"form": form,
		"title": title,
		"text_center": text_center
	}
	
	return render(request, "forms.html", context)










