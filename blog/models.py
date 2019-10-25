# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post_Comment(models.Model):
    user_name = models.CharField(max_length = 50)
    comment = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
