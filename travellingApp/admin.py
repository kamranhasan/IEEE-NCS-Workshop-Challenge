from django.contrib import admin
from .models import Contact, Availability, Booking

# Register your models here.

admin.site.register(Contact)
admin.site.register(Availability)
admin.site.register(Booking)