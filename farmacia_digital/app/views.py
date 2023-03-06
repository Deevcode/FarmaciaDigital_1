from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamentos
from .forms import ContactoForm, MedicamentoForm, CustomUserCreationForm
from django.contrib import messages


from django.contrib.auth import authenticate, login

#VISTA DEL HOME
def home(request):
    return render(request, 'app/home.html')

#VISTA DEL CONTACTO
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)   

#VISTA DE MEDICAMENTOS
def medicamentos(request):
    medicamentos = Medicamentos.objects.all()
    data = {
        'medicamentos' :  medicamentos

    }
    return render(request, 'app/medicamentos.html',data)    

#VISTA DE BODEGA
def bodega(request):
    return render(request, 'app/bodega.html')    

#VISTA DE REPORTE
def reportes(request):
    return render(request, 'app/reporte.html') 

#VISTA DE AGREGAR MEDICAMENTO
def agregar_medicamento(request):
    data = {
        'form' : MedicamentoForm()
    }
    if request.method == 'POST':
        formulario = MedicamentoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Medicamento Registrado")
        else:
            data["form"] = formulario    
    return render(request, 'app/medicamentos/agregar.html', data) 

#VISTA DE LISTAR
def listar_medicamentos(request):
    medicamentos = Medicamentos.objects.all()
    data = {
        'medicamentos' :  medicamentos
    }
    return render(request, 'app/medicamentos/listar.html', data) 

#VISTA DE MODIFICAR
def modificar_medicamento(request, id):
    
    medicamentos = get_object_or_404(Medicamentos, id=id)
    
    data = {
        'form' : MedicamentoForm(instance=medicamentos)
    }

    if request.method == 'POST':
        formulario = MedicamentoForm(data=request.POST, instance=medicamentos, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_medicamento")
        data["form"] = formulario 

    return render(request, 'app/medicamentos/modificar.html', data) 

#VISTA DE ELIMINAR
def eliminar_medicamento(request, id):
    messages.success(request, "Eliminado Correctamente")
    medicamentos = get_object_or_404(Medicamentos, id=id)
    medicamentos.delete()
    return redirect(to="eliminar_medicamento")

#VISTA DE REGISTRO
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redirigir al home
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)