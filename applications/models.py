from django.db import models


class Application(models.Model):
    company = models.TextField(default='')
