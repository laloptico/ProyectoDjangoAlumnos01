from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rodrigo/', views.rodrigo, name='rodrigo'),
    path('miguel/', views.miguel, name='miguel'),
    path('aldo/', views.aldo, name='aldo'),
    path('danielP/', views.danielP, name='danielP'),
    path('danielJ/', views.danielJ, name='danielJ'),
    path('magda/', views.magda, name='magda'),
]
