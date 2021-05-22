from django import forms
from .models import Availability, Booking, Contact
from django import forms


class AvailabilityForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Availability
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
