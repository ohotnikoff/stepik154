from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

class QuestionManager(models.Manager):
    """docstring for QuestionManager"""
    def new(self):
        return super(QuestionManager, self).get_queryset().order_by('added_at')

    def popular(self):
        return super(QuestionManager, self).get_queryset().order_by('rating')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.OneToOneField(User)
