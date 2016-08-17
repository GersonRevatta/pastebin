from django.shortcuts import render
from .models import usuario
from .form import Formul
from django.template.context_processors import csrf
# Create your views here.

def registro(request):
    if request.POST:
        frm = Formul(request.POST)
        if frm.is_valid():
            usuario.crear(frm.username,frm.password)
            HttpResponse('usuario creado')
    else:   
        frm = Formul()


    args = {}
    args.update(csrf(request))
    args['frm'] = frm
    return render (request,'registro.html',args)



