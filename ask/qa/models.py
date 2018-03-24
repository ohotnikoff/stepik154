from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    """docstring for QuestionManager"""
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.OneToOneField(User)

    def __unicode__(self):
        return self.text