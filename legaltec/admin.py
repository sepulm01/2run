from django.contrib import admin
from .models import *
from .utils import clasifica, clasi_new
from .tasks import c_clasifica

# Register your models here.
admin.site.site_header = "LegalTec"
admin.site.index_title = "Menú"
admin.site.site_title = 'LegalTec'

#admin.site.register(lead)

@admin.register(lead)
class LeadAdmin(admin.ModelAdmin):
    actions = [clasi_new]
    list_display = ['nombre','estado','direccion','fono','mail','poliza','aseguradora',]

@admin.register(Preguntas)
class PreguntaAdmin(admin.ModelAdmin):
    #actions = [clasifica]
    list_display = ['pregunta','aseguradora',]

@admin.register(Aseguradora)
class AseguradoraAdmin(admin.ModelAdmin):
    list_display = ['aseguradora',]