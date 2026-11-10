
from django import forms   
from .models import Exception



class ExceptionForm(forms.ModelForm):
    class Meta:
        model = Exception
        fields = '__all__'
        exclude = ['reference', 'id','created_at', 'updated_at'] 
        widgets = {'date_souhaitee': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d')}
