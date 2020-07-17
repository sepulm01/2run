from django.db import models

# Create your models here.

def my_awesome_upload_function(instance, filename):
    return 'lead_{0}/{1}'.format(instance.pk, filename)

class lead(models.Model):
    nombre = models.CharField("Nombre",max_length=30)
    direccion = models.CharField("Direccion",max_length=90)
    fono = models.CharField("Fono",max_length=20)
    mail = models.CharField("email",max_length=40)
    poliza = models.FileField('Poliza',upload_to=my_awesome_upload_function,blank=True, null=True)
    extracto = models.TextField(blank=True, null=True)
    estado = models.BooleanField('Revisado',default=False)
    aseguradora = models.ForeignKey('Aseguradora', on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = "leads"

    def __str__(self):
        return str(self.nombre)

class Aseguradora(models.Model):
    aseguradora = models.CharField("Aseguradora",max_length=120)

    class Meta:
        verbose_name_plural = "Aseguradoras"

    def __str__(self):
        return str(self.aseguradora)

class Preguntas(models.Model):
    pregunta = models.CharField("Pregunta",max_length=120)
    aseguradora = models.ForeignKey('Aseguradora', on_delete=models.PROTECT)
    #segmento = models.ForeignKey('Segmento', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return str(self.pregunta)

class Segmento(models.Model):
    segmento = models.CharField("Segmento",max_length=120, default="Ninguno")
    
    class Meta:
        verbose_name_plural = "Segmentos"

    def __str__(self):
        return str(self.segmento)