from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    stud_class = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="India")

    def __str__(self):
        return self.name
