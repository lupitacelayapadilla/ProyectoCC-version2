from django.contrib.auth.models import User
from django.test import TestCase
from script_grupos import crear_grupos
from usuarios.models import Usuario
from equipos.models import Equipo
from materiales.models import Material, TipoMaterial
from operaciones.models import Operacion

class TestHumo(TestCase):

    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)

    def test_agrega_usuario(self):
        pass

    def test_agrega_operacion(self):
        pass

    def test_agrega_material(self):
        pass

    def test_agrega_equipo(self):
        pass


    

    def test_votacion_exede_calificacion_maxima(self):
        pass

    def test_votacion_exede_calificacion_maxima_mensaje(self):
        pass

    def test_votacion_calificacion_minima(self):
        pass

    def test_votacion_calificacion_minima_mensaje(self):
        pass

    def test_agrega_votacion_verifica_calificacion(self):
        pass
    
    def test_agrega_votacion_verifica_dinosaurio(self):
        pass

    def test_agrega_votacion_verifica_usuario(self):
        pass