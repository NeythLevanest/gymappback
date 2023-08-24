from django.core.validators import RegexValidator
from django.db import models
#Utils
from utils.models import CRideModel
import datetime

class InventPackTable(CRideModel):
    """Profile Model
    Estructura la información pública del usuario
    """
    # userId = models.OneToOneField('app.UserTable', on_delete=models.CASCADE)
    
    # #picture = models.ImageField('Foto de Perfil', upload_to='users/pictures', blank=True, null=True)
    # #biography = models.CharField('Biografía', max_length=500, blank=True, null=True)
    # userId = models.ForeignKey('app.UserTable', on_delete=models.CASCADE)
    dateNum = models.IntegerField('N° Fechas', blank=True, null=True)
    descriptionPack = models.TextField('Descripción', blank=True, null=True)
    priceUnit = models.DecimalField('Precio', max_digits=6, decimal_places=2, blank=True, null=True)

    
    def __str__(self) -> str:
        return self.descriptionPack