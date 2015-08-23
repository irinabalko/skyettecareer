from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg

import os
import uuid

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
	)

def upload_to_workplace(instance, filename):
	blocks = filename.split('.')
	ext = blocks[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	instance.title = blocks[0]
	return os.path.join('uploads/', filename)

# Create your models here.

class Workplace(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(null=True, blank=True)
	city = models.CharField(max_length=300, null=True, blank=True)
	state = models.CharField(max_length=300, null=True, blank=True)
	country = models.CharField(max_length=300, null=True, blank=True)
	website = models.CharField(max_length=300, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="workplace_list", args=[self.id])

	def get_average_overall(self):
		average = self.review_set.all().aggregate(Avg('overall'))['overall__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_paid_parental_leave(self):
		average = self.review_set.all().aggregate(Avg('paid_parental_leave'))['paid_parental_leave__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_reviews(self):
		return self.review_set.all()

	def get_average_female_rolemodels(self):
		average = self.review_set.all().aggregate(Avg('female_rolemodels'))['female_rolemodels__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_salary(self):
		average = self.review_set.all().aggregate(Avg('salary'))['salary__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_flexible_hours(self):
		average = self.review_set.all().aggregate(Avg('flexible_hours'))['flexible_hours__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_telecommuting(self):
		average = self.review_set.all().aggregate(Avg('telecommuting'))['telecommuting__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_average_equal_opportunities(self):
		average = self.review_set.all().aggregate(Avg('equal_opportunities'))['equal_opportunities__avg']
		if average == None:
			return average
		else:
			return int(average)														

class Review(models.Model):
	workplace = models.ForeignKey(Workplace)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	overall = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	paid_parental_leave = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	female_rolemodels = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	salary = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True) 
	flexible_hours = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	telecommuting = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	equal_opportunities = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
