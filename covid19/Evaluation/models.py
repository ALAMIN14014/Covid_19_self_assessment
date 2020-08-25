from django.db import models

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    temperature = models.FloatField()
    score = models.IntegerField()
    pub_date = models.DateField()
    Covid_Result = models.CharField(max_length=100)
