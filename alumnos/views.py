from django.shortcuts import render

def index(request):
    links = [
        {'name': 'rodrigo', 'url': '/rodrigo/'},
        {'name': 'miguel', 'url': '/miguel/'},
        {'name': 'aldo', 'url': '/aldo/'},
        {'name': 'danielP', 'url': '/danielP/'},
        {'name': 'danielJ', 'url': '/danielJ/'},
        {'name': 'magda', 'url': '/magda/'},
        # Agregar los demás enlaces
    ]
    return render(request, 'alumnos/index.html', {'links': links})


def rodrigo(request):
    return render(request, 'alumnos/rodrigo.html')

def miguel(request):
    return render(request, 'alumnos/miguel.html')

def aldo(request):
    return render(request, 'alumnos/aldo.html')

def danielP(request):
    return render(request, 'alumnos/danielP.html')

def danielJ(request):
    return render(request, 'alumnos/danielJ.html')

def magda(request):
    return render(request, 'alumnos/magda.html')
