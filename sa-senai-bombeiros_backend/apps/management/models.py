import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from cuser.models import AbstractCUser
from django.conf import settings


class BrazilianState(models.TextChoices):
    AC = "AC", "Acre"
    AL = "AL", "Alagoas"
    AP = "AP", "Amapá"
    AM = "AM", "Amazonas"
    BA = "BA", "Bahia"
    CE = "CE", "Ceará"
    ES = "ES", "Espírito Santo"
    GO = "GO", "Goiás"
    MA = "MA", "Maranhão"
    MT = "MT", "Mato Grosso"
    MS = "MS", "Mato Grosso do Sul"
    MG = "MG", "Minas Gerais"
    PA = "PA", "Pará"
    PB = "PB", "Paraíba"
    PR = "PR", "Paraná"
    PE = "PE", "Pernambuco"
    PI = "PI", "Piauí"
    RJ = "RJ", "Rio de Janeiro"
    RN = "RN", "Rio Grande do Norte"
    RS = "RS", "Rio Grande do Sul"
    RO = "RO", "Rondônia"
    RR = "RR", "Roraima"
    SC = "SC", "Santa Catarina"
    SP = "SP", "São Paulo"
    SE = "SE", "Sergipe"
    TO = "TO", "Tocantins"
    DF = "DF", "Distrito Federal"

class SexType(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"

class User(AbstractCUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100, help_text="Nome do usuário", verbose_name="Nome"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, null=True, blank=True
    )


    class Meta(AbstractCUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def save(self, **kwargs) -> None:
        return super().save(**kwargs)

    def __str__(self):
        return self.email + " | " + self.first_name + " " + self.last_name

class Admin(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        help_text="Usuário",
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        max_length=50,
        help_text="Telefone principal para contato",
        verbose_name="Telefone",
    )
    cpf = models.CharField(verbose_name="CPF", max_length=20, blank=True, null=True)
    address = models.CharField(
        help_text="Endereço oficial", verbose_name="Endereço", max_length=100
    )
    address_number = models.CharField("Número", max_length=50)
    address_complement = models.CharField(
        "Complemento", max_length=1000, null=True, blank=True
    )
    city = models.CharField(help_text="Cidade", verbose_name="Cidade", max_length=50)
    state = models.CharField(
        help_text="Estado da federação",
        verbose_name="Estado",
        max_length=2,
        choices=BrazilianState.choices,
    )
    zipcode = models.CharField(help_text="CEP", max_length=20)

    def __str__(self):
        return f'Admin {self.id} of user {self.user.name}'

class Firefighter(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        help_text="Usuário",
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        max_length=50,
        help_text="Telefone principal para contato",
        verbose_name="Telefone",
    )
    cpf = models.CharField(verbose_name="CPF", max_length=20, blank=True, null=True)
    address = models.CharField(
        help_text="Endereço oficial", verbose_name="Endereço", max_length=100
    )
    address_number = models.CharField("Número", max_length=50)
    address_complement = models.CharField(
        "Complemento", max_length=1000, null=True, blank=True
    )
    city = models.CharField(help_text="Cidade", verbose_name="Cidade", max_length=50)
    state = models.CharField(
        help_text="Estado da federação",
        verbose_name="Estado",
        max_length=2,
        choices=BrazilianState.choices,
    )
    zipcode = models.CharField(help_text="CEP", max_length=20)

    def __str__(self):
        return f'Firefighter {self.id} of user {self.user.name}'