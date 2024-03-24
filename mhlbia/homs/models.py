from django.db import models
from django.utils import timezone
import random



class Patient(models.Model):
    patient_id = models.CharField(max_length=12, unique=True, editable=False)
    name = models.CharField(max_length=60, name='name')
    age = models.PositiveSmallIntegerField(name='age',)
    date = models.CharField(max_length=5, choices=[('year', 'year'), ('month', 'month'), ('day', 'day')])
    gender = models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')])
    phone = models.CharField(max_length=12, blank=True)
    dr = models.CharField(max_length=30, default='-')
    test = models.ManyToManyField('Test', through='Result')
    entry = models.DateTimeField(default=timezone.now, editable=False)
        
    def generate_rondom(self):
        num = ''.join(str(random.randint(0,9)) for _ in range(12))
        self.patient_id = num
        return self.patient_id
    
    def total_prise(self):
        return sum([query.prise for query in self.test.all()])

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=100)
    prise = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length=100, blank=True)
    ref_male = models.TextField(max_length=5000, blank=True)
    ref_female = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.name

class Result(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.PROTECT)
    result = models.CharField(max_length=20, blank=True)
    ref = models.TextField(max_length=5000, blank=True)
    wrote = models.BooleanField(default=False)
    printed = models.BooleanField(default=False)
    drived = models.BooleanField(default=False)

