from django.db import models


# Create your models here.

class MailList(models.Model):
    name = models.CharField(max_length=90, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
