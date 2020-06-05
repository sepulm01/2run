from django.shortcuts import render
from django.shortcuts import redirect 
from .robot import get_datos

# Create your views here.

def buscar(request):
    def f1(string):
        return any(i.isdigit() for i in string)
    #form = EnvioForm(request.POST)
    if request.method == 'POST':
        formulario = 0
        mensj0 = request.POST['term']
        if f1(mensj0):
            formulario = 1
        persona, para =get_datos(mensj0, formulario)
        #persona = {'nombre': 'Sepulveda Avila Vicente Martin', 'run': '19.688.091-7', 'sex': 'VAR', 'dir': 'Presbitero Moraga 795', 'dist': 'Curacavi'}
        print("paso x aquí EnvioForm", mensj0, formulario)
        #return redirect('/resultado/')
        campos = {
        'form': persona,
        'para': para
         }
        return render(request, 'resultado.html', campos)

    else:
        form = "hola"
    campos = {
    'form': form,
     }
    return render(request, 'buscar.html', campos)

def home(request):
    return redirect('/buscar/')