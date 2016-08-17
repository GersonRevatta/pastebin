from django import forms
from .models import  usuario


class Formul(forms.ModelForm):
	class Meta:
		model = usuario
		fields = ['username','password','email','first_name','last_name']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

		