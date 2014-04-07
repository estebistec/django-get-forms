# -*- coding: utf-8 -*-


from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=512)
    summary = models.TextField()
    keywords = models.CharField(max_length=256)
