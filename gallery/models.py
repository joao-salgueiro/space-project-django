from django.db import models

class Photograph(models.Model):

    OPTIONS_CATEGORY = [
        ("NEBULOSA", "Nebulosa"),
        ("STAR", "Star"),
        ("GALAXY", "Galaxy"),
    ]

    name = models.CharField(max_length=100, null = False, blank=False) #This field cannot be false or blank
    subtitle = models.CharField(max_length=150, null = False, blank=False) #This field cannot be false or blank
    category = models.CharField(max_length=100,choices=OPTIONS_CATEGORY, default="")
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Photograph [name={self.name}]"
