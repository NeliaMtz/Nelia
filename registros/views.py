# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Capturista, Tramite, CT, Visita, Usuario
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django.forms.widgets import DateInput
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



class registrosListar(ListView): 
    model = Visita
    template_name = 'index.html'
    context_object_name = 'registros'
    queryset = Visita.objects.order_by('id')
    paginate_by = 5 # Cambia el número según tus necesidades

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registros = context['registros']
        paginator = Paginator(registros, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            registros_paginados = paginator.page(page)
        except PageNotAnInteger:
            registros_paginados = paginator.page(1)
        except EmptyPage:
            registros_paginados = paginator.page(paginator.num_pages)

        context['registros'] = registros_paginados
        return context
    

class registrosDetalle(DetailView): 
    model = Visita
    

class registrosNuevo(SuccessMessageMixin, CreateView): 
    model = Visita
    form = Visita
    fields = "__all__"
    exclude = ('created_date',)
   
    success_message = 'Visita añadida correctamente.'
   
    # def get_success_url(self):      

    #     return reverse('agreementList')
    
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['fecha_ini'].widget = DateInput(attrs={
    #         'type': 'date',
    #         'class': 'form-control',
    #         'placeholder': 'Fecha de Inicio'
    #     })
    #     form.fields['fecha_fin'].widget = DateInput(attrs={
    #         'type': 'date',
    #         'class': 'form-control',
    #         'placeholder': 'Fecha de Fin'
    #     })
    #     return form
    

class registrosActualizar(SuccessMessageMixin, UpdateView): 
    model = Visita
    form = Visita
    fields = "__all__"

    success_message = 'Visita actualizada correctamente.'
 
    def get_success_url(self):
        return reverse('agreementList')
    

class registrosEliminar(SuccessMessageMixin, DeleteView): 
    model = Visita
    form = Visita
    fields = "__all__"     
 
    def get_success_url(self):
        success_message = 'Visita eliminada correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('agreementList')
    
    