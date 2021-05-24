from django.db import models
from django_countries.fields import CountryField


class Contact(models.Model):
    Name = models.CharField(max_length=100, default="user")
    Email = models.CharField(max_length=50, default="email")
    Subject = models.CharField(max_length=100, default="subject")
    Message = models.CharField(max_length=500, default="message")

    def __str__(self):
        return self.Name


class Booking(models.Model):
    Name = models.CharField(max_length=30, default="")
    date = models.DateField()
    country = CountryField()
    contact = models.CharField(max_length=30, default="")


class Ticket(models.Model):
    Name = models.CharField(max_length=100)
    date = models.DateField()
    country = CountryField()
    picture = models.ImageField(
        upload_to="uploads/places/",
        max_length=100,
        default="uploads/places/dubai.png",
    )
    city = models.CharField(max_length=100, default="Karachi")
    trending = models.BooleanField(default=False)
    price = models.IntegerField(default=15000)
    discount = models.IntegerField(default=0)
    package = models.CharField(max_length=20, default="1 day/night")
    description = models.CharField(
        max_length=300,
        default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    )


class Activity(models.Model):
    Name = models.CharField(max_length=30)
    description = models.CharField(
        max_length=300,
        default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    )


class Hotel(models.Model):
    Name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Karachi")
    picture = models.ImageField(
        upload_to="uploads/hotels/",
        max_length=100,
        default="uploads/hotels/IslamabadHotel.jpg",
    )


class Flight(models.Model):
    locFrom = models.CharField(max_length=30, default="Dubai")
    locTo = models.CharField(max_length=30, default="Karachi")
    price = models.IntegerField(default=100)
    country = CountryField()
    date = models.DateField()
