import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.

class Wartungen(models.Model):
	wartungen_text = models.TextField(max_length=200, verbose_name='Wartungstext')

	startzeit = models.DateTimeField('beginnt:')
	endzeit = models.DateTimeField('endet:')


#	def __init__(self, wartung, startzeit, endzeit):
#		self.w = wartung
#		self.s = startzeit
#		self.e = endzeit

#	def get_text(self):
#		return self.text

#	def get_startzeit(self):
#		return self.startzeit


#	def get_endzeit(self):
#		return self.endzeit

	pub_date = models.DateTimeField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()

		return super(Wartungen, self).save(*args, **kwargs)

	def __str__(self):
		return self.wartungen_text


