from django.db import models

# Create your models here.

class Lab(models.Model):
    pi_name = models.CharField(max_length=200, verbose_name="PI Name")
    university = models.CharField(max_length=200)

    def __unicode__(self):
        return self.university + '-' +  self.pi_name
