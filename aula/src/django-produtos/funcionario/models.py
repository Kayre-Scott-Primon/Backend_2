from django.db import models

# Create your models here.

class Employee(models.Model):
    Gender_options = [
        ("Famale","Famale"),
        ("Male","Male"),
        ("Others","Others")
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bithday = models.DateField()
    document = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    salary = models.FloatField()
    group = models.CharField(max_length=10)
    function = models.CharField(max_length=50)
    initial_at = models.DateField()
    working = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=Gender_options)
    height = models.FloatField()
    weight = models.FloatField()
    observations = models.TextField()

    def __str__(self):
        return self.name