from django.db import models
import datetime

# Model definition
class Poll(models.Model):

    # Model method definitions
    def __unicode__(self):
      return self.question

    def was_published_today(self):
      return self.pub_date.date() == datetime.date.today()

    # Model property definitions
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

class Choice(models.Model):

    # Model method definitions
    def __unicode__(self):
      return self.choice

    # Model property definitions
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()