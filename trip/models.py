#from django.db import models

# Create your models here.
'''from django.db import models


class TripRegistration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    number_of_people = models.PositiveIntegerField()
    food_preference = models.CharField(max_length=20)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
'''

from django.db import models


class TripRegistration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    number_of_people = models.PositiveIntegerField()
    food_preference = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name