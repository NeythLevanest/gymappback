from django.core.validators import RegexValidator
from django.db import models
#Utils
from utils.models import CRideModel
import datetime

class SuitTable(CRideModel):
    """Profile Model
    Estructura la información pública del usuario
    """
    # userId = models.OneToOneField('app.UserTable', on_delete=models.CASCADE)
    
    # #picture = models.ImageField('Foto de Perfil', upload_to='users/pictures', blank=True, null=True)
    # #biography = models.CharField('Biografía', max_length=500, blank=True, null=True)
    namesuit = models.CharField('Nombre', max_length=20, blank=True, null=True)
    descriptionsuit = models.CharField('Descripción', max_length=15, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.namesuit