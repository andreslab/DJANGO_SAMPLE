from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist

def Home(request):
    return render(request, 'index.html')

def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
        print(autor_form)
    return render(request, 'libro/crear_autor.html',{'autor_form_view': autor_form})

def listarAutor(request):
    #autores = Autor.objects.all() # trae todos los objetos sin exeptcion
    autores = Autor.objects.filter(estado = True) #trae solo los datos que tengan el estado True, para que cuando se haga una eliminación logica (el dato solo se oculta de los usuarios) no aparesca 
    return render(request, "libro/listar_autores.html", {"list_autores": autores})

def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance= autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, "libro/crear_autor.html", {'autor_form_view': autor_form, 'error': error})

def eliminarAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        #autor.delete() #eliminacion directa, tanto en el admin como para el usuario
        #eliminacion logica,cambiando el estado para q el usuario no lo visualice
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autores')
    return render(request, "libro/eliminar_autor.html", {'autor': autor})
        
