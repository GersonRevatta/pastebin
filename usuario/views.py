from django.shortcuts import render
from .models import formulario 
from .form import Formul
from django.template.context_processors import csrf
# Create your views here.

def registro(request):
    frm = Formul()

    args = {}
    args.update(csrf(request))

    args['frm'] = frm
    
    return render (request,'registro.html',args)
