from datetime import datetime
from django.db import models

class Photograph(models.Model):

    OPTIONS_CATEGORY = [
        ("NEBULOSA", "Nebulosa"),
        ("STAR", "Star"),
        ("GALAXY", "Galaxy"),
    ]

    name = models.CharField(max_length=100, null = False, blank=False) #This field cannot be false or blank
    subtitle = models.CharField(max_length=150, null = False, blank=False) #This field cannot be false or blank
    category = models.CharField(max_length=100,choices=OPTIONS_CATEGORY, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True) 
    publicated = models.BooleanField(default=False)
    photo_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name
