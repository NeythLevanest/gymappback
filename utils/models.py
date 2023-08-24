from django.db import models

class CRideModel(models.Model):
    """"Modelo Ride 
    Es un modelo abstracto que emplearemos como una clase base
    para otros modelos en donde se requiera controlar la fecha de 
    creación y modificación de un registro
        + created (DateTime): Almacena la fecha en que fue creado un objeto
        + modified (DateTime): Store the last datetime th objects was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add = True,
        help_text = 'Date Time on which the object was created'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now = True,
        help_text = 'Date Time on which the object was last modified'
    )
    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering      = ['-created', '-modified']
        
