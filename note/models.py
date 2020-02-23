from django.db import models

class todo(models.Model):
    content = models.TextField()