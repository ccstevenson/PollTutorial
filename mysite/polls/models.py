import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200) # The field's name. Used as the column name.
    pub_date = models.DateTimeField('date published')

    def __unicode__(self): # Python's __str__() calls __unicode__(), converting the result to a bytestring.
    	return self.question

    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 

class Choice(models.Model):
	# Using Poll as a foreign key ensures that each Choice is related to a single Poll.
	# Django supports all common database relationships: M:M, M:O, O:M.
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self): 
    	return self.choice_text


