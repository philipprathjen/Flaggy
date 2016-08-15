from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model 
from .models import Profile, Country, Memory, CountryCount
from django.conf import settings

User = get_user_model()

# Create your views here.
def profile(request, username):
	user = get_object_or_404(User, username=username)
	active_user = str(request.user)
	profile, created = Profile.objects.get_or_create(user=user)
	username = str(profile)
	
	if request.method =='POST':
		country_code = request.POST['country']
		description = request.POST['description']
		country, created = Country.objects.get_or_create(alpha_two=country_code)
		instance = Memory(user = user, country = country)
		instance.description = description
		instance.save()

	country_count = CountryCount.objects.filter(user=user)
	country_count_dict = dict()
	for item in country_count:
		key = str(item.country)
		value = item.count
		country_count_dict[key] = value

	context = {
		"username": username,
		"country_count_dict": country_count_dict, 
		"active_user": active_user,
		"profile": profile,
	}

	return render(request, "profile.html", context)
