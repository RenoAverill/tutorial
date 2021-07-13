from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.


class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return f'''
            ID = {self.id},
            cohort_name = {self.cohort_name},
            start_date = {self.start_date},
            end_date = {self.end_date}
        '''


class Student(models.Model):
    cohort = models.ForeignKey(
        Cohort, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'''
            id = {self.id},
            first_name = {self.first_name},
            last_name = {self.last_name}
        '''
