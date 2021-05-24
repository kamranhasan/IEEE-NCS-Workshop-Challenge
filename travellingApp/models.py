from django.db import models


class Contact(models.Model):
    Name = models.CharField(max_length=100, default="user")
    Email = models.CharField(max_length=50, default="email")
    Subject = models.CharField(max_length=100, default="subject")
    Message = models.CharField(max_length=500, default="message")

    def __str__(self):
        return self.Name


class Availability(models.Model):
    date = models.DateField()
    country = models.CharField(max_length=30, default="Pakistan")


class Booking(models.Model):
    Name = models.CharField(max_length=30, default="")
    date = models.DateField()
    country = models.CharField(max_length=30, default="Pakistan")
    contact = models.CharField(max_length=30, default="")


class Ticket(models.Model):
    Name = models.CharField(max_length=100)
    date = models.DateField()
    country = models.CharField(max_length=30, default="Pakistan")
    picture = models.ImageField(upload_to="uploads/", max_length=100)
    city = models.CharField(max_length=100, default="Karachi")
    trending = models.BooleanField(default=False)
    price = models.IntegerField(default=15000)
    discount = models.IntegerField(default=0)
    package = models.CharField(max_length=20, default="1 day/night")
    description = models.CharField(
        max_length=400,
        default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    )
