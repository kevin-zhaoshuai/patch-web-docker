from django.db import models

# Create your models here.
class Kernel_Project(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=75)
	datetime=models.DateTimeField("date commited")
	comment=models.CharField(max_length=1000)
	hashvalue=models.CharField(max_length=10)

class Libvirt_Project(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=75)
	datetime=models.DateTimeField("date commited")
	comment=models.CharField(max_length=1000)
	hashvalue=models.CharField(max_length=10)

class OpenStack_Project(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=75)
	datetime=models.DateTimeField("date commited")
	comment=models.CharField(max_length=1000)
	hashvalue=models.CharField(max_length=10)
