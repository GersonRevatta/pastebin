from django.shortcuts import render

from .forms import ArticuloForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
import hashlib
from .models import reporte 

from django.core.urlresolvers import reverse
# Create your views here.


#def Reporte(request):
 #   return render(request,'template.html')

#hola
def crear(request):
    if request.POST:
        form = ArticuloForm(request.POST)
        if form.is_valid():
                       

            a = form.save()
            a.codigo = hashlib.md5(str(a.id).encode()).hexdigest()[:5]
            a.save()

            return HttpResponseRedirect(reverse('must',args=(a.codigo,)))
    else:
        form = ArticuloForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request,'template.html', args)

def mostrar(request , codigo):

    r = reporte.objects.get(codigo=codigo)

    return render (request,'hola.html', {'reporte': r})