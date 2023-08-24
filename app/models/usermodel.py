#Django
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator

from gymapp import settings

import datetime

#Utils
from utils.models import CRideModel


"""User Model Manager"""
class UserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        #username = self.model.normalize_username(username)
        user = self.model(username = email,
                             email = email,
                             **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_activate', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(
            email = email,
            username = username,
            password= password,
            **extra_fields
        )
        user.usuario_administrador = True
        user.save()
        return user


class UserTable(CRideModel, AbstractUser):

    """User Model
    Extend from Django's Abstract User, change the username field to email and add some extra fields
    """

    email = models.EmailField(
        'emailAddres', 
        unique=True,
        error_messages = {
            'unique': 'A user with that email already exist.'
            }
    )

    """UserType Model       
    Estructura la información pública del usuario
    """
    # naturePerson = 'Persona Natural'
    # legalPerson = 'Persona Jurídica'
    # user_type_list = [(naturePerson, 'Persona Natural'), 
    #          (legalPerson, 'Person Jurídica')]
    # user_type = models.CharField(max_length=20, choices=user_type_list, default=naturePerson)

    """Validate user state"""
    is_staff = models.BooleanField(
        'staff status',
        default = False,
        help_text = 'Designates whether the user can log into this'
    )
    
    is_activate = models.BooleanField(
        'active',
        default = False,
        help_text = 'Set to true when the user have active its email address.'
    )

    is_active = models.BooleanField(
        'active',
        default = False,
        help_text = 'Set to true when the user have active its email address.'
    )

    is_verified = models.BooleanField(
        'verified',
        default = False,
        help_text = 'Set to true when the user have verified its email address.'
    )

    #data_joined = models.DateTimeField('date joined', blank=True, null=True, default=datetime.datetime.now().time())

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    """Def Function"""
    def __str__(self):
        return str(self.id)

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self
    def user(self):
        return self
