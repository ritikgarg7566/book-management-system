from django.db import models
from django.contrib.auth.models import User

class bookm(models.Model):
    username=models.CharField(max_length=10)
    title=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    bookfile=models.FileField(null=True)
    filetype=models.CharField(max_length=20)
    aname=models.CharField(max_length=20)
    pname=models.CharField(max_length=20)

