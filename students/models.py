from django.db import models

# Create your models here.

#from django.db import models

import datetime
from django.utils import timezone

class Student(models.Model):
    student_firstName = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # ...
    def __str__(self):
        return self.student_firstName


    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Telefon(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    telefon_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.telefon_text
