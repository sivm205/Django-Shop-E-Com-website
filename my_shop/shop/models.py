from django.db import models
from django.contrib.auth.models import User

class shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    category = models.CharField(max_length=50)
    est_year = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name