from django import forms

#We are creating the form for the signup model
# This is all we have to do for the signup form as fr using it in our admin goes. 
from .models import SignUp

# Creating a contact form
class ContactForm(forms.Form):
	#No model Form, we dont need a model
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()
	def clean_email(self):
		email=self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please use valid USC email address") 
		if not extension == "edu":
			raise forms.ValidationError("Please use valid college email address") 
		return email


#The form goes throught the validations
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name", "email"]
		# exclude = ['full_name'] ##use sparingly. More difficult to follow

# We want to check the email data
# This is called a validator for a field
	def clean_email(self):
		email=self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please use valid USC email address") 
		if not extension == "edu":
			raise forms.ValidationError("Please use valid college email address") 
		return email

		#print(self.cleaned_data)
		#return "abc@gmail.com"

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name') 
		# Write validation code
		return full_name