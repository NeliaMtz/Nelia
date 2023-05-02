from django.db import models
from django.utils import timezone 
from datetime import datetime

 
# Create your models here.


class CT(models.Model):
    CT = models.CharField(max_length=10,primary_key=True)
    Nombre_CT = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_CT

class Usuario(models.Model):
    CURP= models.CharField(max_length=18,primary_key=True)
    Nombres = models.CharField(max_length=50)
    Ap_Pat = models.CharField(max_length=50)
    Ap_Mat = models.CharField(max_length=50)
    Edad = models.CharField(max_length=3)
    Cve_Ct = models.ForeignKey(CT, on_delete=models.CASCADE)
    Escolaridad = models.CharField(max_length=50)
    Funcion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.CURP

class Capturista(models.Model):
    CURP_Cap = models.CharField(max_length=18,primary_key=True)
    Nombre = models.CharField(max_length=50)
    Puesto = models.CharField(max_length=50)

    def __str__(self):
            return self.CURP_Cap

class Tramite(models.Model):
    Descripcion = models.CharField(max_length=50)
   
    def __str__(self):
            return self.Descripcion
    
    
class Visita(models.Model):
      #Modelo para registrar_visita usuario# https://es.stackoverflow.com/questions/121867/implementaci%C3%B3n-hora-y-fecha-en-django
    #dia  = models.DateTimeField(auto_now_add=True)
    #hora = models.DateTimeField(auto_now_add=True)
    #dia = datetime.now()

    #formatodDia  = dia.strftime('%d %B, %Y')
    #FormatodHora = dia.strftime('%H:%M')

    CURP = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #Fecha = models.CharField(max_length=50, default=formatodDia)
    #Fecha = dia
    #Fecha = models.DateTimeField(auto_now_add=True)
    Fecha = models.CharField(max_length=50)
    Hora_ini = models.CharField(max_length=50)
    Hora_fin = models.CharField(max_length=50)
    id_tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE)
    CURP_Cap = models.ForeignKey(Capturista, on_delete=models.CASCADE)
    
    def __str__(self):
        template = '{0.id}, {0.CURP}, {0.Fecha}, {0.Hora_ini}, {0.Hora_fin}, {0.id_tramite}, {0.CURP_Cap}'
        return template.format(self)
    #    #    return self.id    
  