from django.contrib import admin
from .models import Profile, Country, CountryCount, Memory, Award
# Register your models here.


admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(CountryCount)
admin.site.register(Memory)
admin.site.register(Award)