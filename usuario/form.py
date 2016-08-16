
from .models import  formulario


class Formu(forms.ModelForm):
	class Meta:
		model = formulario
		fields = ['username','password','email','first_name','last_name']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

		