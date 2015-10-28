from django.db import models


class AppList(models.Model):
    pass


class Application(models.Model):
    company = models.TextField(default='')
    app_list = models.ForeignKey(AppList, default=None)
