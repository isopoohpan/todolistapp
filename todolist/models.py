from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Todo(models.Model):
	TIME_SLOT_CHOICES = (
		('MO', 'Moring'),
		('AF', 'Afternoon'),
		('EV', 'Evening'),
		('NI', 'Night'),
	)

	title = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	members = models.ManyToManyField(Member)
	timeslot = models.CharField(max_length=2, choices=TIME_SLOT_CHOICES,default='MO')
	published = models.BooleanField(default=False)

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ('title',)



