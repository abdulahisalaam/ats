from django.db import models

# Create your models here.
class About_me(models.Model):
    """Model representing a company profile"""
    firstname = models.CharField(max_length=20, help_text='Firstname (e.g. Abdullah)')

    lastname = models.CharField(max_length=20, help_text='Lastname (e.g. Salaam)')

    age = models.DateField(help_text='your age (e.g. 30)')

    programming_language = models.CharField(max_length=15, help_text='programming language (e.g. python)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

