from django.contrib.auth.models import User
from django.test import TestCase
from usuarios.models import Usuario 
from usuarios.forms import UsuarioFormLog, UsuarioForm
from equipos.models import Equipo
from materiales.models import Material, TipoMaterial
from operaciones.models import Operacion
from operaciones.forms import OperacionForm
from django.core.exceptions import ValidationError


class TestFormUsuario(TestCase):

    def setUp(self, nombre='isaacdiaz', matricula='34123456',
              password='Contra12345', saldo='100', password_re='Contra12345'):
        self.usuario = Usuario(
            username=nombre,
            matricula=matricula,
            saldo=saldo,
            is_superuser= True,
            password=password
        )

        self.data = {
            'username': nombre,
            'matricula': matricula,
            'saldo': saldo,
            'is_superuser': True,
            'password': password
        }

        self.data_admin = {
            'nombre': 'isaacdiaz',
            'usuario': self.usuario.id
        }

        

    # TEST PARA USUARIO
    def test_usuario_form_valido(self):
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UsuarioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_matricula_invalida_vacia(self):
        self.data['matricula'] = ''
        form = UsuarioForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['matricula'],
            ['This field is required.'])

  #  def test_usuario_form_matricula_invalida(self):
  #      self.data['matricula'] = 'afgh'
  #      form = UsuarioForm(self.data)
  #      self.assertNotRegex('afgh', "[0-9]{8}", )
  #      self.assertEqual(
  #          form.errors['matricula'],
  #          ['Utiliza un formato que coincida con el solicitado.'])

    def test_usuario_form_password_re_formato_invalido(self):
        self.data['password_re'] = 'contra'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Contra12345'
        self.data['password_re'] = '12345Contra'
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_mas_caracteres(self):
        self.data['username'] = 'isaacdiaz'*15
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_password_re_mas_caracteres(self):
        self.data['password_re'] = 'Contra12345'*15
        form = UsuarioForm(self.data)
        self.assertTrue(form.is_valid())

    # TEST LOGIN

    def test_form_login_valido(self):
        self.crear_usuario()
        form = UsuarioFormLog(
            None, data={'username': 'isaacdiaz', 'password': 'Contra12345'})
        self.assertTrue(form.is_valid())

    def test_form_login_invalido(self):
        self.crear_usuario()
        form = UsuarioFormLog(
            None, data={'username': 'isaacdiaz', 'password': 'Contra12345'})
        self.assertFalse(form.is_valid())






            
    def crear_usuario(self):
        User.objects.create_user(
            username='isaacdiaz',
            password='Contra12345'
        )



class TestFormOperaciones(TestCase):

    def setUp(self, nombre='imprimir', precio_unitario='2',
              cantidad='100', material='hoja oficio'):
        self.operacion = Operacion(
            nombre=nombre,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            material= material
        )

        self.data = {
            'nombre': nombre,
            'precio_unitario': precio_unitario,
            'cantidad': cantidad,
            'material': material
        }

    # TEST PARA OPERACIONES
    def test_operacion_form_valido(self):
        form = OperacionForm(self.data)
        self.assertTrue(form.is_valid())

    def test_operacion_form_nombre_vacio(self):
        self.data['nombre'] = ''
        form = OperacionForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_operacion_form_precio_vacio(self):
        self.data['precio'] = ''
        form = OperacionForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_operacion_form_cantidad_vacio(self):
        self.data['cantidad'] = ''
        form = OperacionForm(self.data)
        self.assertFalse(form.is_valid())

    def test_operacion_form_material_vacio(self):
        self.data['material'] = ''
        form = OperacionForm(self.data)
        self.assertFalse(form.is_valid())

    def test_operacio_form_precio_invalido(self):
        self.data['precio'] = 'hola'
        form = OperacionForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['precio'],
            ['This field is required.'])




class TestFormMateriales(TestCase):
    pass

class TestFormEquipos(TestCase):
    pass