from django.db import models

# Create your models here.
class Customer(models.Model):
	uname = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	psw = models.CharField(max_length=20)

	def __str__(self):
		return self.uname