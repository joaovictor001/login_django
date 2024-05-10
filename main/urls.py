from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.abre_index, name= 'abre_index'),
    path('cadastro/<int:id>',views.cadastro, name="cadastro"),
    path('gravar',views.gravar, name="gravar"),
    path('excluir/<int:id>',views.excluir, name="excluir"),
]