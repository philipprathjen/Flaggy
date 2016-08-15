from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

# Create your models here.


User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
	extension = filename.split(".")[1]
	location = instance.user.username
	return '%s/profile.%s' %(location, extension)

class Country(models.Model):
	# countryname = models.CharField(max_length = 120, null = True, blank= True)
	# OneToOneField any user can only have one profile. Kind of a unique clause
	alpha_two = models.CharField(max_length = 2, null = True, blank= True)

	def __str__(self):
		return self.alpha_two

	def get_absolute_url(self):
		url = reverse('country', kwargs={'username': self.countryname}) 
		#This actually

class CountryCount(models.Model):
	user = models.ForeignKey(User)
	country = models.ForeignKey(Country)
	count = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.user) + "_" + str(self.country)

class Memory(models.Model):
	user = models.ForeignKey(User)
	country = models.ForeignKey(Country)
	description = models.CharField(max_length = 10000, null = True, blank= True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return str(self.user) + "_" + str(self.country)

@receiver(post_save, sender=Memory)
def add_country_code(sender, **kwargs):
    if kwargs.get('created', False):
    	user = kwargs.get('instance').user
    	country = kwargs.get('instance').country
    	countrycount, created = CountryCount.objects.get_or_create(user=user, country=country)
    	count = countrycount.count 
    	print(count)
    	if count == None:
    		count = 1
    	else:
    		count += 1
    	print(count)
    	countrycount.count = count
    	countrycount.save()

@receiver(post_save, sender=Memory)
def grant_triple_maghreb_crown(sender, **kwargs):
	if kwargs.get('created', False):
		user = kwargs.get('instance').user
		country = kwargs.get('instance').country
		award = Award.objects.get(name="Maghreb Triple Crown")
		x = 0
		try:
			algeria = Country.objects.get(alpha_two="DZ")
			countrycount, created = CountryCount.objects.get_or_create(user=user, country=algeria)
			x += 1
			print(x)
		except:
			pass
		try:
			morocco = Country.objects.get(alpha_two="MA")
			countrycount, created = CountryCount.objects.get_or_create(user=user, country=morocco)
			x += 1
			print(x)
		except:
			pass
		try:
			tunisia = Country.objects.get(alpha_two="TN")
			countrycount, created = CountryCount.objects.get_or_create(user=user, country=tunisia)
			x += 1
			print(x)
		except:
			pass
		if x == 3:
			user_profile = Profile.objects.get(user=user)
			user_profile.award = award
			user_profile.save()
			print("Halleluja") 



class Award(models.Model):
	name = models.CharField(max_length=120, null=True, blank=True)
	country_combo = models.ManyToManyField(Country)
	description = models.CharField(max_length = 10000, null = True, blank= True)

	def __str__(self):
		return str(self.name)

class Profile(models.Model):
	user = models.OneToOneField(User)
		# OneToOneField any user can only have one profile. Kind of a unique clause
	location = models.CharField(max_length = 120, null=True, blank=True)
	picture = models.ImageField(upload_to =upload_location, null=True, blank = True)
	award = models.ForeignKey(Award, null=True, blank=True)

	def __str__(self):
		return self.user.username	

	def get_absolute_url(self):
		url = reverse('profile', kwargs={'username': self.user.username}) 
		#This actually gives us the URL
		return url




