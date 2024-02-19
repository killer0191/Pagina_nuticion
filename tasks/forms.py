from django import forms
from .models import Task,Sobrepeso, Localidad, Curso


#Se crea la clase de los formularios que llenarán los usuarios.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['matricula', 'nombre','apellidos', 'edad','estatura','talla','peso','actividad_fisica',
                'imc',]
        widgets = {
            'matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matricula escolar'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'Escriba sus apellidos (ap-am)'}),
            'edad': forms.NumberInput(attrs={'class':'form-control'}),
            'estatura': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Colóque su estatura en metros (m)'}),
            'talla': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Colóque su talla (XS, S, M, G, L, XL, XLL)'}),
            'peso': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Colóque su peso en kilogramos (kg)'}),
            'actividad_fisica': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'imc': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
class TaskSobrepeso(forms.ModelForm):
    class Meta:
        model= Sobrepeso
        fields=['tipo','estilo_vida',]
        widgets= {
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'estilo_vida': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sedentaria, semi-activa, activa'}),
        }

class TaskLocalidad(forms.ModelForm):
    class Meta:
        model= Localidad
        fields=['cp','estrato','region_ensanut',]
        widgets={
            'cp': forms.TextInput(attrs={'class':'form-control'}),
            'estrato': forms.TextInput(attrs={'class':'form-control'}),
            'region_ensanut': forms.TextInput(attrs={'class':'form-control'}),
        }

class TaskCurso(forms.ModelForm):
    class Meta:
        model= Curso
        fields=['nombre_curso','grado',]
        widgets= {
            'nombre_curso': forms.TextInput(attrs={'class':'form-control'}),
            'grado': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Grado en texto, no en número'}),
        }

