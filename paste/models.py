from django.db import models
from usuario.models import usuario

# Create your models here.

class reporte (models.Model):
	cuerpo = models.TextField()
	fecha  = models.DateTimeField(auto_now_add=True)
	codigo = models.CharField(max_length=5)
	usuario = models.ForeignKey(usuario,null=True, blank=True)
	
	# Yay
	def __str__(self):
		#codigo = hashlib.md5(str(self.id)).hexdigest()[:5]
		
		return str(self.cuerpo[0:10])



class formulario (models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email =  models.EmailField()
	first_name = models.CharField(max_length=30)
	last_name =models.CharField(max_length=30)





	
