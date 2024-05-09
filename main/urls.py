from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.abre_index, name= 'abre_index'),
    path('cadastro/<int:id>',views.cadastro, name="cadastro"),
    path('listar',views.listar, name="listar"),
     path('excluir/<int:id>',views.excluir, name="excluir"),
]