from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Revenue(models.Model):
	MonthlyRevenue = models.CharField(max_length=50)
	Month = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s' % (self.MonthlyRevenue, self.Month)

class City(models.Model):
	Name = models.CharField(max_length=50)
	CountryCode = models.CharField(max_length=50)
	Population = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s %s' % (self.Name, self.CountryCode, self.Population)

class Country(models.Model):
	Name = models.CharField(max_length=50)
	Code = models.CharField(max_length=50)
	Population = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s %s' % (self.Name, self.Code, self.Population)
						