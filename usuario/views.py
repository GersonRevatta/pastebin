from django.shortcuts import render
from .models import usuario
from .form import Formul
from django.template.context_processors import csrf
# Create your views here.
from django.http import HttpResponse
def registro(request):
	user=password=''
	if request.POST:
		frm = Formul(request.POST)
		if frm.is_valid():
			a = usuario.crear.objects.get(username,password)
			usuario.crear(a.username,a.password)
			usuario.save()
			
			return HttpResponse('Cuenta guardada')
		else:
			a=usuario.crear( user= request.POST['username'], password =request.POST['password'])

			return HttpResponse('¿?')
	else:   
		frm = Formul()

	args = {}
	args.update(csrf(request))
	args['frm'] = frm
	return render (request,'registro.html',args)

def loguin(request):
	...
#	user=password=''
#	if request.POST:
#		c = Formul(request.POST)
#		if c.is_valid:
#			c  =	usuario.verificar( user= request.POST['username'], password =request.POST['password'])
#			b	=	usuario.verificar.get()
#			if c==True:
#				return  HttpResponse('es valido')
#			else:	
#				return  HttpResponse('intenta otra vez')
#		
#	else:
#		c=Formul()
#	args = {}
#	args.update(csrf(request))
#	args['c'] = c
#	return render(request,'cuenta.html',args )
	

