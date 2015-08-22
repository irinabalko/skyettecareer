from django.db import models
from django.core.urlresolvers import reverse

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