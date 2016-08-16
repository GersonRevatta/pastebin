from django.db import models

class formulario (models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email =  models.EmailField()
	first_name = models.CharField(max_length=30)
	last_name =models.CharField(max_length=30)





# Create your models here.
