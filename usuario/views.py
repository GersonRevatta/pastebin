from django.shortcuts import render
from .models import usuario
from .form import Formul
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template.context_processors import csrf
# Create your views here.
from django.http import HttpResponse



from paste.models import reporte
def registro(request):
	user=password=''
	if request.POST:
		frm = Formul(request.POST)
		if frm.is_valid():
			
			a= usuario.crear( user= request.POST['username'], password =request.POST['password'])
			a.first_name = frm.cleaned_data['first_name']
			a.email =frm.cleaned_data['email']
			a.last_name =frm.cleaned_data['last_name']

			a.save()
			return HttpResponseRedirect(reverse('loguin'))		
			
	else:   
		frm = Formul()

	args = {}
	args.update(csrf(request))
	args['frm'] = frm
	return render (request,'registro.html',args)

def logout(request):
	user=password=''
	if request.POST:
		c = Formul(request.POST)
		if c.is_valid:
			c  =	usuario.verificar( user= request.POST['username'], password =request.POST['password'])

			if c==True:
				
				z = request.POST['username']		
					#return render(request,test.html,args)
				request.session['userr']=z	
				

				return HttpResponseRedirect(reverse('create'))

			else:	
				

				return  HttpResponseRedirect(reverse('loguin'))
				
	else:
		c=Formul()
	args = {}
	args.update(csrf(request))
	args['c'] = c

	# try:
	# 	request.session['contador'] += 1		
	# except:
	# 	request.session['contador'] = 0

	# args['contador'] = request.session['contador']

	return render(request,'cuenta.html',args )



def logoutt(request):
	try:
		del request.session['userr']
	except KeyError:
		pass

	return HttpResponseRedirect(reverse('create'))



def listar(request):
	try:
		lis = usuario.objects.get(username=request.session['userr'])
		lts=reporte.objects.filter(usuario=lis)
		return render(request,'lista.html', {'lts':lts})
		
	except :
		pass
	
	#lis = usuario.objects.get(username=request.session['userr'])
	#lts=reporte.objects.filter(usuario=lis)
	return HttpResponseRedirect(reverse('create'))
	#return render(request,'lista.html', {'lts':lts})
#aprender a comentar de una mera mas ordenada