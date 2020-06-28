from django.contrib import admin
from .models import *
from .utils import clasifica

# Register your models here.
admin.site.site_header = "LegalTec"
admin.site.index_title = "Menú"
admin.site.site_title = 'LegalTec'

#admin.site.register(lead)

@admin.register(lead)
class LeadAdmin(admin.ModelAdmin):
    actions = [clasifica]
    list_display = ['nombre','estado','direccion','fono','mail','poliza',]

@admin.register(Preguntas)
class PreguntaAdmin(admin.ModelAdmin):
    actions = [clasifica]
    list_display = ['pregunta',]