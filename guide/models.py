from django.db import models


# Create your models here.

class RegForm(models.Model):
    restaurants = (
        ('Paradise', 'Paradise'),
        ('Park Hyatt', 'Park Hyatt'),
        ('Mariott', 'Mariott'),
        ('Radisson', 'Radisson'),
        ('Novotel', 'Novotel'),
        ('Hyatt Place', 'Hyatt Place'),
    )
    restaurant = models.CharField(max_length=50, choices=restaurants)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    attendies = models.IntegerField(blank=True)
    comments = models.TextField(blank=True)
