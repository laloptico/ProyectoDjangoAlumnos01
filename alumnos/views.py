from django.shortcuts import render

def index(request):
    return render(request, 'alumnos/index.html', {'links': []})
