from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Name', required=True, max_length=100)
    
    email=forms.CharField(label='Email', required=True, max_length=50)
    
    contenido=forms.CharField(label='Content', required=True, max_length=100, widget=forms.Textarea)