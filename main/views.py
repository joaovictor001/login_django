from django.shortcuts import render
from .models import Pessoas
from django.shortcuts import render

def abre_index(request):
    return render(request, 'index.html')

def gravar(request):
    if(request.method == 'POST'):
        nome= request.POST.get('nome')
        idade= request.POST.get('idade')

        gravaCadastro = Pessoas(
            nome=nome,
            idade=idade

        )
        gravaCadastro.save()


def listar(request):
        usuarios = Pessoas.objects.all()
        return render (request ,'index.html', {'lista_usuarios':usuarios})

def cadastro(request, id):
    novo_registro = Pessoas.objects.filter(id=id)
    nome = novo_registro[0].nome  
    idade = novo_registro[0].idade  
    print(novo_registro)
    return render(request, 'cadastro.html', {'novo_registro': novo_registro, 'idade': idade, 'nome': nome,'novo_ID':id})

def editar(request):
     id= request.POST.get('id')
     nome = request.POST.get('nome')
     idade = request.POST.get('idade')
     pessoa = Pessoas.objects.filter(id = id)
     gravar_dados = pessoa(
        nome = nome,
        idade= idade
     )

     gravar_dados.save()

     return render(request,'index.html')

def excluir(request, id):
    pessoa = Pessoas.objects.filter(id = id)
    pessoa.delete()
    return render(request,'index.html')



     

    

