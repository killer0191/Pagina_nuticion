from django.contrib import admin
from .models import Task
from .models import Sobrepeso
from .models import Localidad
from .models import Curso

#Si se deseara un campo de SOLO LECTURA
#class TaskAdmin(admin.ModelAdmin):
#   readonly_fields = ('tupladesololectura', ')
#admin.site.register(Task, TaskAdmin)

# Register your models here.
# Permitir que se muestren las tablas o modelos creados, en la interfaz admin de Django
admin.site.register(Task)
admin.site.register(Sobrepeso)
admin.site.register(Localidad)
admin.site.register(Curso)
