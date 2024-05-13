from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Rather not say", "Rather not say"),
)

class GetStarted(models.Model):
    firstname = models.CharField(max_length= 122)
    lastname = models.CharField(max_length= 122)
    gender = models.CharField(
        max_length = 20,
        choices = GENDER_CHOICES,
        default = '1',
        null=True
        )
    email = models.CharField(max_length= 122)
    contact = models.CharField(max_length= 10)
    city = models.CharField(max_length= 122)


    def __str__(self):
        return self.firstname

