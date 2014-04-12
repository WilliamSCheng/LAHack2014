from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hangout(models.Model):
  # user1 = models.CharField(max_length=50)
  #  user2 = models.CharField(max_length=50)
  user1 = models.ForeignKey('User')
  user2 = models.ForeignKey('User')
  location = models.CharField(max_length=100)
  duration = models.CharField(max_length=50)

  def __unicode__(self):
    return 'Hangout between ' + str(self.user1) + ' and ' + str(self.user2)