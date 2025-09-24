from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib import admin
from .models import Usuario

admin.site.register(Usuario)

def home(request):
    return render(request, 'usuarios/h.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Verifica se o nome já está cadastrado
        if Usuario.objects.filter(nome=nome).exists():
            return render(request, 'usuarios/h.html', {
                'erro': 'Este nome já está cadastrado!'
            })

        # Salva o novo usuário
        Usuario.objects.create(nome=nome, idade=idade)

    contexto = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', contexto)

def deletar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    usuario.delete()
    return render(request, 'usuarios/usuarios.html', {'usuarios': Usuario.objects.all()})
