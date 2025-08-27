from django.contrib import admin
from .models import UserProfile, TravelOption, Booking

admin.site.register(UserProfile)
admin.site.register(TravelOption)
admin.site.register(Booking)
