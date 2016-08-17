from django import forms
from .models import  formulario


class Formul(forms.ModelForm):
	class Meta:
		model = formulario
		fields = ['username','password','email','first_name','last_name']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

		