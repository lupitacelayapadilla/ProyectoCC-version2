from .models import Operacion
from usuarios.models import Usuario
from .forms import OperacionForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required, permission_required


class OperacionList(ListView):
    paginate_by = 5
    model = Operacion
    context_object_name = 'operaciones'
    extra_context = {'etiqueta': 'Lista', 'oper_list': True}


"""class OperacionCrear(CreateView):

    model = Operacion
    form_class = OperacionForm
    extra_context = {'etiqueta':'Registrar', 'boton':'Agregar', 'oper_new':True, 'user':request.user.get_username()}
    success_url = reverse_lazy('operacion:lista')"""


def nueva_operacion(request):
    nombre = ''
    precio_unitario = ''
    cantidad = ''
    usuario = -1
    material = None
    form = OperacionForm(request.POST)
    if form.is_valid():
        patternNombre ="^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
        nombre = form.cleaned_data.get("nombre")
        precio_unitario = form.cleaned_data.get("precio_unitario")
        cantidad = form.cleaned_data.get("cantidad")
        usuario = Usuario.objects.get(id=request.user.id)
        material = form.cleaned_data.get("material")
        oper = Operacion(
            nombre=nombre,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            usuario=usuario,
            material=material)
        oper.save()
        return redirect('operaciones:lista')
    context = {'form': form, "cat_nueva": True, 'etiqueta': 'Crear'}
    return render(request, 'operaciones/operacion_form.html', context)


class OperacionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'usuarios.cajero_permiso'
    model = Operacion
    extra_context = {'etiqueta': 'Eliminar', 'op_del': True}
    success_url = reverse_lazy('operaciones:lista')


class OperacionDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'usuarios.cajero_permiso'
    model = Operacion
    extra_context = {
        'etiqueta': 'Detalles',
        'boton': 'Regresar',
        'mt_det': True}


"""def validar_matricula(request):
    matricula = request.GET
    context = {'matricula':matricula,"cat_nueva":True}
    return render(request, 'operaciones/operacion_form.html', context)"""


"""class OperacionEditar(UpdateView):
    model = Operacion
    form_class = OperacionForm
    extra_context = {'etiqueta':'Editar', 'boton':'Guardar', 'edit_equipo':True}
    success_message = "El equipo se actualizó con exito"
    success_url = reverse_lazy('operacion:lista')

class OperacionDelete(DeleteView):
    model = Operacion
    extra_context = {'etiqueta':'Eliminar', 'del_equipo':True}
    success_url = reverse_lazy('operacion:lista')

class OperacionDetail(DetailView):
    model = Operacion
    extra_context = {'etiqueta':'Detalles', 'boton':'Regresar', 'det_equipo':True}"""
