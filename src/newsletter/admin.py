from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

# This allows us to customize how the admin works
# We want to configure what we see
# Check out how you can modify admin page:
# https://docs.djangoproject.com/en/1.9/ref/contrib/admin/
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	form = SignUpForm
	#class Meta: 	
	#	model= SignUp



admin.site.register(SignUp, SignUpAdmin)