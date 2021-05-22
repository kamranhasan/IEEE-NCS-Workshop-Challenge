from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100, default='user')
    Email = models.CharField(max_length=50, default='email')
    Subject = models.CharField(max_length=100, default='subject')
    Message = models.CharField(max_length=500, default='message')
    def __str__(self):
        return self.Name