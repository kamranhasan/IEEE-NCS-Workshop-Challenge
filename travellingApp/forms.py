from django import forms
from .models import Booking, Contact, Flight
from django import forms
from django_countries.widgets import CountrySelectWidget


class FlightForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Flight
        fields = ("date", "country")


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Booking
        fields = ("Name", "date", "country", "contact")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "Name",
            "Email",
            "Subject",
            "Message",
        )
