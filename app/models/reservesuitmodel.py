from django.core.validators import RegexValidator
from django.db import models
#Utils
from utils.models import CRideModel
import datetime

class ReserveTable(CRideModel):
    """Profile Model
    Estructura la información pública del usuario
    """
    userId = models.ForeignKey('app.UserTable', on_delete=models.CASCADE)
    suitId = models.ForeignKey('app.SuitTable', on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    createdDate = models.DateTimeField(auto_now_add=True)
    remainingChanges = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"Reserva de {self.suitId} para {self.userId}"    