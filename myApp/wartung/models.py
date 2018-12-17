import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.

class Wartungen(models.Model):
	wartungen_name = models.CharField(max_length=50, verbose_name='Wartungsname')
	wartungen_text = models.TextField(max_length=200, verbose_name='Wartungstext')
	domain = models.CharField(max_length=100, verbose_name='Domain')
	startzeit = models.DateTimeField('beginnt:')
	endzeit = models.DateTimeField('endet:')




	pub_date = models.DateTimeField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()

		return super(Wartungen, self).save(*args, **kwargs)

	def __str__(self):
		return self.wartungen_text




