from django.contrib import admin
from .models import Contact, Availability, Booking, Ticket, Activity, Hotel

# Register your models here.

admin.site.register(Contact)
admin.site.register(Availability)
admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(Activity)
admin.site.register(Hotel)