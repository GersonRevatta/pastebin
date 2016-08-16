from django import forms
from .models import reporte, formulario

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = reporte
        fields = ['cuerpo']

class Formu(forms.ModelForm):
	class Meta:
		model = formulario
		fields = ['username','password','email','first_name','last_name']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

		