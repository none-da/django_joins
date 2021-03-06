"""
Question Title
Question Description
Question Comments count
All Answers descriptions
All Answer comments
Answer author names
Assuming I have a hover action on the Author Link, which displays information like: Followers count, Mentions count, Reputation Score
"""

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    raised_by = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
class Answer(models.Model):
    description = models.CharField(max_length=500, blank=True, null=True)
    given_by = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    
    def __unicode__(self):
        return self.description

class QuestionComment(models.Model):
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    
class AnswerComment(models.Model):
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    
class Reputation(models.Model):
    user = models.ForeignKey(User)
    points = models.IntegerField(default=0)

class Follower(models.Model):
    user = models.ForeignKey(User)
    following = models.ForeignKey(User, related_name='all_followers')
    
class Mention(models.Model):
    user = models.ForeignKey(User, related_name='all_mentions')
    count = models.IntegerField(default=0)