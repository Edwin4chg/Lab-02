from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'calculadora/operacion.html', context)

def res(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    operacion = request.POST['operacion']
    resultado = 0
    
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2

    context = {
        'titulo': "Resultado",
        'resultado': resultado,
        'num1': num1,
        'num2': num2,
        'operacion': operacion,
    }
    return render(request, 'calculadora/resultado.html', context)
