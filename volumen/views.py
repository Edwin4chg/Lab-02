from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'volumen/formulario.html', context)

def cal(request):    
    diametro = float(request.POST['diametro']) 
    altura = float(request.POST['altura'])  
    
    radio = diametro/2
    pi = 3.14159
    volumen = pi * (radio**2)  * altura

    context = {
        'volumen' : volumen,
    }
    return render(request, 'volumen/resultados.html', context)
    
