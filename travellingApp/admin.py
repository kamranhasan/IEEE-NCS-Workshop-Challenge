from django.contrib import admin
from .models import Contact, Booking, Ticket, Activity, Hotel, Flight

# Register your models here.

admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(Activity)
admin.site.register(Hotel)
admin.site.register(Flight)