from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm

def inicio(request):
    notas = Nota.objects.all()
    context = {'notas': notas}
    return render(request, 'todo/inicio.html', context)

def crear(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = NotaForm()
    context = {'form': form}
    return render(request, 'todo/crear.html', context)

def borrar(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    nota.delete()
    return redirect("inicio")

def modificar(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = NotaForm(instance=nota)
    context = {'form': form}
    return render(request, 'todo/modificar.html', context)
