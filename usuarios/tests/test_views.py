from django.contrib.auth.models import User
from django.test import TestCase
from script_grupos import crear_grupos
from usuarios.models import Usuario
from equipos.models import Equipo
from materiales.models import Material, TipoMaterial
from operaciones.models import Operacion


class TestViews(TestCase):
    def setUp(self):
        crear_grupos()

    ###ADMINISTRADOR - USUARIOS

    def test_admin_ingresa_lista_usuarios(self):
        self.login_admin()
        response = self.client.get('/usuarios/lista/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_nuevo_usuario(self):
        self.login_admin()
        response = self.client.get('/usuarios/nuevo/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_editar_usuario(self):
        self.login_admin()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_template_correcto_lista_usuario(self):
        self.login_admin()
        response = self.client.get('/usuarios/lista/')
        self.assertTemplateUsed(response, 'usuarios/usuario_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_editar_usuario(self):
        self.login_admin()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'editar_usuario.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_nuevo_usuario(self):
        self.login_admin()
        response = self.client.get('/usuarios/nuevo/')
        self.assertTemplateUsed(response, 'usuarios/usuario_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    ### Admin - Equipos

    def test_admin_ingresa_lista_equipos(self):
        self.login_admin()
        response = self.client.get('/equipos/lista/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_nuevo_equipo(self):
        self.login_admin()
        response = self.client.get('/equipos/nuevo/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_editar_equipo(self):
        self.insertar_equipo()
        self.login_admin()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_ingresa_url_detalle_equipo(self):
        self.insertar_equipo()
        self.login_admin()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_template_correcto_lista_equipos(self):
        self.login_admin()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'equipos/equipo_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    ###ADMINISTRADOR - OPERACIONES

    def test_admin_ingresa_lista_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/lista/')
        self.assertEqual(response.status_code, 200)

    def test_admin_template_correcto_lista_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_nuevo_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_lista_operaciones(self):
        self.login_admin()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_admin_template_correcto_nuevo_operacion(self):
        self.login_admin()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    ###ADMINISTRADOR - TIPOMATERIAL
    def test_admin_ingresa_url_tipoMaterial(self):
        self.insertar_tipoMaterial()
        self.login_admin()
        response = self.client.get('/tipomaterial/lista/')
        self.assertEqual(response.status_code, 200)

    ###ADMINISTRADOR - MATERIALES

    def test_admin_ingresa_lista_materiales(self):
        self.login_admin()
        response = self.client.get('/materiales/lista/')
        self.assertEqual(response.status_code, 200)

    ###CAJERO - USUARIOS

    def test_cajero_ingresa_lista_usuarios(self):
        self.login_cajero()
        response = self.client.get('/usuarios/lista/')
        self.assertEqual(response.status_code, 200)

    def test_cajero_ingresa_url_nuevo_usuario(self):
        self.login_cajero()
        response = self.client.get('/usuarios/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_ingresa_url_editar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_correcto_lista_usuario(self):
        self.login_cajero()
        response = self.client.get('/usuarios/lista/')
        self.assertTemplateUsed(response, 'usuarios/usuario_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_incorrecto_editar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_template_incorrecto_nuevo_usuario(self):
        self.login_cajero()
        response = self.client.get('/usuarios/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_ingresa_eliminar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/eliminar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_incorrecto_eliminar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/eliminar/' + str(last.id))
        self.assertTemplateUsed(response, '403.html')

    def test_cajero_template_correcto_eliminar_usuario(self):
        self.login_cajero()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/eliminar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')

    ###CAJERO - EQUIPO

    def test_cajero_ingresa_lista_equipos(self):
        self.login_cajero()
        response = self.client.get('/equipos/lista/')
        self.assertEqual(response.status_code, 200)

    def test_cajero_ingresa_url_nuevo_equipo(self):
        self.login_cajero()
        response = self.client.get('/equipos/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_ingresa_url_editar_equipo(self):
        self.insertar_equipo()
        self.login_cajero()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_cajero_ingresa_url_detalle_equipo(self):
        self.insertar_equipo()
        self.login_cajero()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertEqual(response.status_code, 200)

    def test_cajero_template_correcto_lista_equipos(self):
        self.login_cajero()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'equipos/equipo_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_correcto_lista_equipos(self):
        self.login_cajero()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'equipos/equipo_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_incorrecto_nuevo_equipo(self):
        self.login_cajero()
        response = self.client.get('/equipos/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    ### CAJERO - OPERACIONES

    def test_cajero_ingresa_lista_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/lista/')
        self.assertEqual(response.status_code, 200)

    def test_cajero_template_correcto_lista_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_correcto_nuevo_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_cajero_template_incorrecto_lista_operaciones(self):
        self.login_cajero()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

     ### CAJERO - TIPOMATERIAL

    def test_cajero_ingresa_url_tipoMaterial(self):
        self.insertar_tipoMaterial()
        self.login_cajero()
        response = self.client.get('/tipomaterial/lista/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_incorrecto_tipomaterial_lista(self):
        self.login_cajero()
        response = self.client.get('/tipomaterial/lista/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    ### CAJERO - MATERIALES

    def test_cajero_ingresa_lista_materiales(self):
        self.login_cajero()
        response = self.client.get('/materiales/lista/')
        self.assertEqual(response.status_code, 403)

    def test_cajero_template_incorrecto_materiales_lista(self):
        self.login_cajero()
        response = self.client.get('/materiales/lista/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

 ###ALUMNO - USUARIOS

    def test_alumno_ingresa_lista_usuarios(self):
        self.login_alumno()
        response = self.client.get('/usuarios/lista/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_nuevo_usuario(self):
        self.login_alumno()
        response = self.client.get('/usuarios/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_editar_usuario(self):
        self.login_alumno()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_alumno_template_incorrecto_usuario_lista(self):
        self.login_alumno()
        response = self.client.get('/usuarios/lista/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_incorrecto_usuario_nuevo(self):
        self.login_alumno()
        response = self.client.get('/usuarios/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_incorrecto_usuario_editar(self):
        self.login_alumno()
        last = Usuario.objects.latest('id')
        response = self.client.get('/usuarios/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')
        self.assertTemplateUsed(response, '403.html')

    ### ALUMNO - EQUIPOS

    def test_alumno_ingresa_lista_equipos(self):
        self.login_alumno()
        response = self.client.get('/equipos/lista/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_nuevo_equipo(self):
        self.login_alumno()
        response = self.client.get('/equipos/nuevo/')
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_editar_equipo(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_alumno_ingresa_url_detalle_equipo(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertEqual(response.status_code, 403)

    def test_alumno_template_incorrecto_lista_equipo(self):
        self.login_alumno()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_correcto_lista_equipo(self):
        self.login_alumno()
        response = self.client.get('/equipos/lista/')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_incorrecto_nuevo_equipos(self):
        self.login_alumno()
        response = self.client.get('/equipos/nuevo/')
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_correcto_nuevo_equipos(self):
        self.login_alumno()
        response = self.client.get('/equipos/nuevo/')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_equipos_detaller(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_incorrecto_equipos_detaller(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/detalles/' + str(last.id))
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_incorrecto_equipos_editar(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertTemplateUsed(response, '403.html')

    def test_alumno_template_correcto_equipos_editar(self):
        self.insertar_equipo()
        self.login_alumno()
        last = Equipo.objects.latest('id')
        response = self.client.get('/equipos/editar/' + str(last.id))
        self.assertTemplateUsed(response, 'base2.html')

    ### ALUMNO - OPERACIONES

    def test_alumno_ingresa_lista_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/lista/')
        self.assertEqual(response.status_code, 200)

    def test_alumno_template_correcto_lista_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_nuevo_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_lista_operaciones(self):
        self.login_alumno()
        response = self.client.get('/operaciones/lista/')
        self.assertTemplateUsed(response, 'operaciones/operacion_list.html')
        self.assertTemplateUsed(response, 'base2.html')

    def test_alumno_template_correcto_nuevo_operacion(self):
        self.login_alumno()
        response = self.client.get('/operaciones/nuevo/')
        self.assertTemplateUsed(response, 'operaciones/operacion_form.html')
        self.assertTemplateUsed(response, 'base2.html')

     ### CAJERO - TIPOMATERIAL

    def test_alumno_ingresa_url_tipoMaterial(self):
        self.insertar_tipoMaterial()
        self.login_alumno()
        response = self.client.get('/tipomaterial/lista/')
        self.assertEqual(response.status_code, 403)

    ### CAJERO - MATERIALES

    def test_alumno_ingresa_lista_materiales(self):
        self.login_alumno()
        response = self.client.get('/materiales/lista/')
        self.assertEqual(response.status_code, 403)

    ####### Funciones ########

    def login_admin(self):
        self.client.login(username='administrador', password='administrador')

    def login_cajero(self):
        self.client.login(username='cajero', password='cajero')

    def login_alumno(self):
        self.client.login(username='alumno', password='alumno')

    def insertar_equipo(self):
        equipo = Equipo.objects.create(tipo='impresora', marca='hp', modelo="uaz",
                                       disponibilidad='D')

    def insertar_tipoMaterial(self):
        material = TipoMaterial.objects.create(nombre='hojas oficio')
