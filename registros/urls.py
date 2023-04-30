from django.contrib import admin
from django.urls import path
from registros.views import  registrosListar, registrosDetalle, registrosNuevo, registrosActualizar,registrosEliminar
from django.conf.urls.static import static

urlpatterns = [
    path('registros/', registrosListar.as_view(template_name = "registros/list.html"), name='agreementList'),   
    path('registros/detail/<int:pk>', registrosDetalle.as_view(template_name = "registros/details.html"), name='agreementDetails'),
    path('registros/add', registrosNuevo.as_view(template_name = "registros/create.html"), name='agreementCreate'),
    path('registros/update/<int:pk>', registrosActualizar.as_view(template_name = "registros/update.html"), name='agreementUpdate'), 
    path('registros/eliminar/<int:pk>', registrosEliminar.as_view(), name='agreementDelete'),    
]