from django import forms
from .models import Task, Sobrepeso, Localidad, Curso

# Se crea la clase de los formularios que llenarán los usuarios.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['matricula', 'nombre', 'apellidos', 'edad', 'estatura', 'talla', 'peso', 'actividad_fisica', 'imc']
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricula escolar'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba sus apellidos (ap-am)'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estatura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Colóque su estatura en metros (m)'}),
            'talla': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('XS', 'Extra Pequeña'),
                ('S', 'Pequeña'),
                ('M', 'Mediana'),
                ('G', 'Grande'),
                ('L', 'Extra Grande'),
                ('XL', 'Extra Extra Grande'),
                ('XXL', 'Extra Extra Extra Grande'),
            ]),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Colóque su peso en kilogramos (kg)'}),
            'actividad_fisica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imc': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TaskSobrepeso(forms.ModelForm):
    class Meta:
        model = Sobrepeso
        fields = ['tipo', 'estilo_vida']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'estilo_vida': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('sedentaria', 'Sedentaria'),
                ('semi-activa', 'Semi-activa'),
                ('activa', 'Activa'),
            ]),
        }

class TaskLocalidad(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = ['cp', 'estrato', 'region_ensanut']
        widgets = {
            'cp': forms.TextInput(attrs={'class': 'form-control'}),
            'estrato': forms.TextInput(attrs={'class': 'form-control'}),
            'region_ensanut': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TaskCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'grado']
        widgets = {
            'nombre_curso': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('primero', 'Primero'),
                ('segundo', 'Segundo'),
                ('tercero', 'Tercero'),
                ('cuarto', 'Cuarto'),
                ('quinto', 'Quinto'),
                ('sexto', 'Sexto'),
                ('septimo', 'Séptimo'),
                ('octavo', 'Octavo'),
                ('noveno', 'Noveno'),
                ('decimo', 'Décimo'),
            ]),
        }
