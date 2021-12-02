from django.db import models
from django.core.validators import MinValueValidator
#from usuario.models import Usuario


class Operacion(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=False)
    precio_unitario = models.DecimalField(
        'Precio Unitario',
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0)])
    cantidad = models.IntegerField(
        'Cantidad', default=1, validators=[
            MinValueValidator(1)])

    #precio_total = models.DecimalField('Precio Total',decimal_places=2,max_digits=5,min_value=0)

    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        "usuarios.Usuario",
        verbose_name="Usuario",
        on_delete=models.CASCADE)
    material = models.ForeignKey(
        "materiales.TipoMaterial",
        verbose_name="Material",
        on_delete=models.CASCADE)

    def get_precio_total(self):
        return cantidad * precio_unitario

    def __str__(self):
        return self.nombre
