from django.db import models

class List(models.Model):
    image = models.ImageField(upload_to="images/")