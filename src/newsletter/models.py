from django.db import models
#This is where we will be storing most of our data
# Create your models here.
# Documentation here: https://docs.djangoproject.com/en/1.9/ref/models/fields/
# To add a model to the database go to settings.py
# IN TERMINAL: 
# python manage.py makemigrations 
# python manage.py migrate

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	#We have to set a unicode
	def __str__(self):
		return self.email