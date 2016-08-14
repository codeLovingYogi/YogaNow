from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class YogaClass(models.Model):
    studio = models.ForeignKey(Studio)
    teacher = models.ForeignKey(Teacher)
    description = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.description

