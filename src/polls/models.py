import datetime

from django.db import models
from django.utils import timezone

# Create your models here
class Question(models.Model):
    '''
    Db table for questions.
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        '''Check if question is recently published, i.e. within last 24 hours'''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    '''
    Db table for choices.

    Multiple choices can be associated with one question.
    This is example of Many to one relationship ManyToOne from choices to question
    and One to many relationship from question to choices.
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
