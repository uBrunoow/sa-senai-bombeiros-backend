import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from django.conf import settings
from apps.management.models import User, Firefighter
from django.core.exceptions import ValidationError


class SexType(models.TextChoices):
    MALE = 'MALE', 'Masculino'
    FEMALE = 'FEMALE', 'Feminino'


class SizeType(models.TextChoices):
    EIGHT = '8', '8'
    TWELVE = '12', '12'
    TWENTY = '20', '20'
    H = 'H', 'H'
    P = 'P', 'P'
    O = 'O', 'O'
    G = 'G', 'G'
    N = 'N', 'N'
    PP = 'PP', 'PP'
    M = 'M', 'M'
    ADULTO = 'ADULTO', 'ADULTO'
    INFANTIL = 'INFANTIL', 'INFANTIL'


class Report(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='news_posts', verbose_name="Usuário")
    report_date = models.DateTimeField(
        verbose_name="Data do relatório", help_text="Data do relatório", null=True, blank=True)
    name = models.CharField(max_length=100, help_text="Nome da vítima",
                            verbose_name="Nome", null=True, blank=True)
    general_registration = models.CharField(
        max_length=100, help_text="RG/CPF do paciente", verbose_name="RG/CPF do paciente", null=True, blank=True)
    age = models.IntegerField(
        help_text="Idade da vítima", verbose_name="Idade", null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SexType.choices,
                           help_text="Sexo", verbose_name="Sexo", null=True, blank=True)
    escort = models.CharField(max_length=100, help_text="Acompanhante",
                              verbose_name="Acompanhante", null=True, blank=True)
    escort_age = models.IntegerField(
        help_text="Idade do acompanhante", verbose_name="Idade do acompanhante", null=True, blank=True)
    report_place = models.CharField(max_length=100, help_text="Local do acidente",
                                    verbose_name="Local do acidente", null=True, blank=True)
    phone = models.CharField(max_length=100, help_text="Telefone para contato",
                             verbose_name="Telefone para contato", null=True, blank=True)
    type_of_occurrence = models.ManyToManyField(
        "TypeOfOccurrence", related_name='reports', blank=True, verbose_name="Tipo de ocorrência")
    other_occurrence = models.TextField(
        help_text="Descrição para outros tipos de ocorrências", verbose_name="Outro Tipo de ocorrência", null=True, blank=True)
    suspect_problems = models.ManyToManyField(
        'SuspectProblems', related_name='reports', blank=True, verbose_name="Problemas suspeitos")
    sub_suspect_problems = models.ManyToManyField(
        'SubSuspectProblems', related_name='reports', blank=True, verbose_name="Sub-Problemas suspeitos")
    other_problems = models.TextField(
        help_text="Descrição para outros problemas", verbose_name="Outros problemas", null=True, blank=True)
    signs_and_symptoms = models.ManyToManyField(
        "SignsAndSymptoms", related_name='reports', blank=True, verbose_name="Sinais e sintomas")
    sub_signs_and_symptoms = models.ManyToManyField(
        "SubSignsAndSymptoms", related_name='reports', blank=True, verbose_name="Sub-Sinais e sintomas")
    sub_sub_signs_and_symptoms = models.ManyToManyField(
        "SubSubSignsAndSymptoms", related_name='reports', blank=True, verbose_name="Sub-Sub-Sinais e sintomas")
    other_signs_and_symptoms = models.TextField(
        help_text="Descrição para outros sinais e sintomas", verbose_name="Outros sinais e sintomas", null=True, blank=True)
    glasgow = models.ForeignKey(
        "Glasgow", on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    vital_signs = models.ForeignKey(
        "VitalSigns", on_delete=models.CASCADE, related_name='reports', blank=True, null=True, verbose_name="Sinais vitais")
    driving_style = models.ManyToManyField(
        "DrivingStyle", related_name='reports', blank=True, verbose_name="Forma de condução")
    victim_was = models.ManyToManyField(
        "VictimWas", related_name='reports', blank=True, verbose_name="Vítima era")
    decision_transport = models.ManyToManyField(
        "TransportDecision", related_name='reports', blank=True, verbose_name="Decisão de transporte")
    service_team = models.ForeignKey(
        "ServiceTeam", on_delete=models.CASCADE, related_name='reports', blank=True, null=True, verbose_name="Time de serviço")
    objects_recovered = models.TextField(
        help_text="Objetos recuperados", verbose_name="Objetos recuperados", null=True, blank=True)
    transport_informations = models.ForeignKey(
        "TransportInformations", on_delete=models.CASCADE, related_name='reports', blank=True, null=True, verbose_name="Informações de transporte")
    proceeding = models.ManyToManyField(
        "Proceeding", related_name='reports', blank=True, verbose_name="Procedimento")
    sub_proceeding = models.ManyToManyField(
        "SubProceeding", related_name='reports', blank=True, verbose_name="Sub-Procedimento")
    sub_sub_proceeding = models.ManyToManyField(
        "SubSubProceeding", related_name='reports', blank=True, verbose_name="Sub-Sub-Procedimento")
    other_proceeding = models.TextField(
        help_text="Descrição para outros procedimentos", verbose_name="Outro procedimento", null=True, blank=True)
    observations = models.TextField(
        help_text="Observações", verbose_name="Observações", null=True, blank=True)
    anamnesis = models.ForeignKey(
        "Anamnesis", on_delete=models.CASCADE, related_name='reports', blank=True, null=True, verbose_name="Anamnese")
    gestacional_anamnesis = models.ForeignKey(
        "GestacionalAnamnesis", on_delete=models.CASCADE, related_name='reports', blank=True, null=True, verbose_name="Anamnese gestacional")
    cinematic = models.ForeignKey(
        "Cinematic", on_delete=models.CASCADE, related_name='reports', blank=True, null=True, verbose_name="Avaliação de Cinemática")
    disposable_materials = models.ManyToManyField(
        "DisposableMaterials", related_name='reports', blank=True, verbose_name="Materiais descartáveis")
    other_disposable_materials = models.TextField(
        help_text="Descrição para outros materiais descartáveis", verbose_name="Outros materiais descartáveis", null=True, blank=True)
    quantity_other_disposable_materials = models.IntegerField(
        help_text="Quantidade de outros materiais descartáveis", verbose_name="Quantidade de outros materiais descartáveis", null=True, blank=True)
    hospital_materials = models.ManyToManyField(
        "HospitalMaterials", related_name='reports', blank=True, verbose_name="Materiais hospitalares")
    other_hospital_materials = models.TextField(
        help_text="Descrição para outros materiais hospitalares", verbose_name="Outros materiais hospitalares", null=True, blank=True)
    quantity_other_materials = models.IntegerField(
        help_text="Quantidade de outros materiais hospitalares", verbose_name="Quantidade de outros materiais hospitalares", null=True, blank=True)
    responsable_for_report = models.CharField(
        max_length=100, help_text="Responsável pelo relatório", verbose_name="Responsável pelo relatório", null=True, blank=True)

    def __str__(self):
        return "A ocorrência de " + self.name + " foi registrada por " + str(self.user) + " as " + str(self.created_at)

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class TypeOfOccurrence(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Tipo de ocorrência", verbose_name="Tipo de ocorrência")

    def __str__(self):
        return "Tipo de ocorrência | " + self.name

    class Meta:
        verbose_name = "Tipo de Ocorrência"
        verbose_name_plural = "Tipos de Ocorrência"


class SuspectProblems(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Problema suspeito | " + self.name

    class Meta:
        verbose_name = "Problema Suspeito"
        verbose_name_plural = "Problemas Suspeitos"


class SubSuspectProblems(BaseModel):
    name = models.CharField(max_length=100)
    suspect_problem = models.ForeignKey(
        SuspectProblems, on_delete=models.CASCADE)

    def __str__(self):
        return "Sub-Problema suspeito | " + str(self.suspect_problem.name) + " | " + self.name

    class Meta:
        verbose_name = "Sub-Problema Suspeito"
        verbose_name_plural = "Sub-Problemas Suspeitos"


class SignsAndSymptoms(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Sintoma  | " + self.name

    class Meta:
        verbose_name = "Sintoma"
        verbose_name_plural = "Sintomas"


class SubSignsAndSymptoms(BaseModel):
    name = models.CharField(max_length=100)
    signs_and_symptoms = models.ForeignKey(
        SignsAndSymptoms, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.signs_and_symptoms) + " | " + self.name

    class Meta:
        verbose_name = "Sub-Sintoma"
        verbose_name_plural = "Sub-Sintomas"


class SubSubSignsAndSymptoms(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Sinais e sintomas", verbose_name="Sinais e sintomas")
    sub_signs_and_symptoms = models.ForeignKey(
        SubSignsAndSymptoms, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sub_signs_and_symptoms) + " | " + self.name

    class Meta:
        verbose_name = "Sub-Sub-Sintoma"
        verbose_name_plural = "Sub-Sub-Sintomas"


class SubSubProceeding(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Procedimento", verbose_name="Procedimento")
    sub_proceeding = models.ForeignKey(
        "SubProceeding", on_delete=models.CASCADE, related_name='sub_sub_proceedings')

    def __str__(self):
        return str(self.sub_proceeding) + " | " + self.name

    class Meta:
        verbose_name = "Sub-Sub-Procedimento"
        verbose_name_plural = "Sub-Sub-Procedimentos"


class SubProceeding(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Procedimento", verbose_name="Procedimento")
    proceeding = models.ForeignKey('Proceeding', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.proceeding) + " | " + self.name

    class Meta:
        verbose_name = "Sub-Procedimento"
        verbose_name_plural = "Sub-Procedimentos"


class Proceeding(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Procedimento", verbose_name="Procedimento")
    proceed_value = models.IntegerField(
        help_text="Valor", verbose_name="Valor", null=True, blank=True)

    def __str__(self):
        return "Procedimento | " + self.name

    class Meta:
        verbose_name = "Procedimento"
        verbose_name_plural = "Procedimentos"

# TODO: Rever estes campos de glasgow


class GlasgowType(BaseModel):
    name = models.CharField(max_length=100, help_text="Tipo de Glasgow",
                            verbose_name="Tipo de Glasgow", null=True, blank=True)
    is_grater_than_five_year = models.BooleanField(
        help_text="Maior que cinco anos", verbose_name="Maior que cinco anos", null=True, blank=True)
    eye_opening = models.BooleanField(
        help_text="Abertura ocular", verbose_name="Abertura ocular", null=True, blank=True)
    verbal_response = models.BooleanField(
        help_text="Resposta verbal", verbose_name="Resposta verbal", null=True, blank=True)
    motor_response = models.BooleanField(
        help_text="Resposta motora", verbose_name="Resposta motora", null=True, blank=True)
    value = models.IntegerField(
        help_text="Valor", verbose_name="Valor", null=True, blank=True)

    def __str__(self):
        return "Glasgow | " + self.name


class Glasgow(BaseModel):
    eye_opening = models.IntegerField(
        help_text="Abertura ocular", verbose_name="Abertura ocular", null=True, blank=True)
    verbal_response = models.IntegerField(
        help_text="Resposta verbal", verbose_name="Resposta verbal", null=True, blank=True)
    motor_response = models.IntegerField(
        help_text="Resposta motora", verbose_name="Resposta motora", null=True, blank=True)
    total = models.IntegerField(
        help_text="Total", verbose_name="Total", null=True, blank=True)

    def __str__(self):
        return 'Glasgow com total | ' + str(self.total)

    def save(self, *args, **kwargs):
        eye_opening = self.eye_opening if self.eye_opening is not None else 0
        verbal_response = self.verbal_response if self.verbal_response is not None else 0
        motor_response = self.motor_response if self.motor_response is not None else 0

        self.total = eye_opening + verbal_response + motor_response
        super(Glasgow, self).save(*args, **kwargs)


class VitalSigns(BaseModel):
    heart_rate = models.IntegerField(
        help_text="Frequência cardíaca", verbose_name="Frequência cardíaca", null=True, blank=True)
    respiratory_rate = models.IntegerField(
        help_text="Frequência respiratória", verbose_name="Frequência respiratória", null=True, blank=True)
    blood_pressure = models.IntegerField(
        help_text="Pressão arterial", verbose_name="Pressão arterial", null=True, blank=True)
    temperature = models.IntegerField(
        help_text="Temperatura", verbose_name="Temperatura", null=True, blank=True)
    saturation = models.IntegerField(
        help_text="Saturação", verbose_name="Saturação", null=True, blank=True)
    pulse = models.IntegerField(
        help_text="Pulso", verbose_name="Pulso", null=True, blank=True)
    perfusion_is_greater_than_two_seconds = models.BooleanField(
        help_text="Perfusão maior que dois segundos", verbose_name="Perfusão maior que dois segundos", null=True, blank=True)
    is_normal = models.BooleanField(
        help_text="Normal", verbose_name="Normal", null=True, blank=True)

    def __str__(self):
        return "Sinais vitais | " + str(self.id)

    class Meta:
        verbose_name = "Sinal Vital"
        verbose_name_plural = "Sinais Vitais"


class DrivingStyle(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Estilo de direção", verbose_name="Estilo de direção")

    def __str__(self):
        return "Forma de transporte | " + self.name

    class Meta:
        verbose_name = "Forma de Transporte"
        verbose_name_plural = "Formas de Transportes"


class VictimWas(BaseModel):
    title = models.CharField(
        max_length=100, help_text="Título", verbose_name="Título")

    def __str__(self):
        return "Vítima era | " + self.title

    class Meta:
        verbose_name = "Vítima"
        verbose_name_plural = "Vítimas"


class TransportDecision(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Decisão de transporte", verbose_name="Decisão de transporte")

    def __str__(self):
        return "Decisão de transporte | " + self.name

    class Meta:
        verbose_name = "Decisão de Transporte"
        verbose_name_plural = "Decisões de Transporte"


class ServiceTeam(BaseModel):
    name_m = models.ForeignKey(
        Firefighter, on_delete=models.CASCADE, related_name='service_team_m', verbose_name="M", null=True, blank=True
    )
    name_s1 = models.ForeignKey(
        Firefighter, on_delete=models.CASCADE, related_name='service_team_s1', verbose_name="S1", null=True, blank=True
    )
    name_s2 = models.ForeignKey(
        Firefighter, on_delete=models.CASCADE, related_name='service_team_s2', verbose_name="S2", null=True, blank=True
    )
    name_demandante = models.ForeignKey(
        Firefighter, on_delete=models.CASCADE, related_name='service_team_demandante', verbose_name="Demandante", null=True, blank=True
    )
    name_team = models.CharField(
        max_length=100, help_text="Equipe", verbose_name="Equipe", null=True, blank=True
    )

    def __str__(self):
        return "Time de serviço | " + self.name_team

    class Meta:
        verbose_name = "Equipe de atendimento"
        verbose_name_plural = "Equipe de atendimento"


class TransportInformations(BaseModel):
    number_usb = models.IntegerField(
        help_text="Número USB", verbose_name="Número USB", null=True, blank=True)
    num_occurencies = models.IntegerField(
        help_text="Número de ocorrências", verbose_name="Número de ocorrências", null=True, blank=True)
    desp = models.CharField(max_length=100, help_text="Despachante",
                            verbose_name="Despachante", null=True, blank=True)
    ir_cod = models.BooleanField(
        help_text="Código IR", verbose_name="Código IR", null=True, blank=True)
    ps_cod = models.BooleanField(
        help_text="Código PS", verbose_name="Código PS", null=True, blank=True)
    sia_sus_cod = models.BooleanField(
        help_text="Código SIA/SUS", verbose_name="Código SIA/SUS", null=True, blank=True)
    final_km = models.IntegerField(
        help_text="KM final", verbose_name="KM final", null=True, blank=True)
    hch = models.CharField(max_length=100, help_text="HCH",
                           verbose_name="HCH", null=True, blank=True)

    def __str__(self):
        return "Informações de transporte | " + str(self.number_usb)

    class Meta:
        verbose_name = "Informações de transporte"
        verbose_name_plural = "Informações de transporte"


class Anamnesis(BaseModel):
    what_happend = models.TextField(
        help_text="O que aconteceu", verbose_name="O que aconteceu", null=True, blank=True)
    happend_other_times = models.BooleanField(
        help_text="Aconteceu outras vezes", verbose_name="Aconteceu outras vezes", null=True, blank=True)
    how_long_happend = models.CharField(
        max_length=100, help_text="Quanto tempo aconteceu", verbose_name="Quanto tempo aconteceu", null=True, blank=True)
    health_problems = models.BooleanField(
        help_text="Problemas de saúde", verbose_name="Problemas de saúde", null=True, blank=True)
    health_problems_description = models.TextField(
        help_text="Descrição de problemas de saúde", verbose_name="Descrição de problemas de saúde", null=True, blank=True)
    alergies = models.BooleanField(
        help_text="Alergias", verbose_name="Alergias", null=True, blank=True)
    alergies_description = models.TextField(
        help_text="Descrição de alergias", verbose_name="Descrição de alergias", null=True, blank=True)
    medications = models.BooleanField(
        help_text="Medicamentos", verbose_name="Medicamentos", null=True, blank=True)
    medications_description = models.TextField(
        help_text="Descrição de medicamentos", verbose_name="Descrição de medicamentos", null=True, blank=True)
    hour_of_last_medication = models.CharField(
        max_length=100, help_text="Hora da última medicação", verbose_name="Hora da última medicação", null=True, blank=True)
    drank_liquid_food = models.BooleanField(
        help_text="Líquidos e alimentos ingeridos", verbose_name="Líquidos e alimentos ingeridos", null=True, blank=True)
    hour_of_last_drank_liquid_food = models.CharField(max_length=100, help_text="Hora da última ingestão de líquidos e alimentos",
                                                      verbose_name="Hora da última ingestão de líquidos e alimentos", null=True, blank=True)

    def __str__(self):
        return "Anamnsese | " + str(self.created_at) + " | " + self.what_happend

    class Meta:
        verbose_name = "Anamnese"
        verbose_name_plural = "Anamneses"


class GestacionalAnamnesis(BaseModel):
    gestational_period = models.CharField(
        max_length=100, help_text="Período gestacional", verbose_name="Período gestacional", null=True, blank=True)
    pre_natal = models.BooleanField(
        help_text="Pré-natal", verbose_name="Pré-natal", null=True, blank=True)
    complications = models.BooleanField(
        help_text="Complicações", verbose_name="Complicações", null=True, blank=True)
    first_child = models.BooleanField(
        help_text="Primeira gestação", verbose_name="Primeira gestação", null=True, blank=True)
    number_of_children = models.IntegerField(
        help_text="Número de filhos", verbose_name="Número de filhos", null=True, blank=True)
    time_of_contractions = models.CharField(max_length=100, help_text="Que horas iniciaram as contrações",
                                            verbose_name="Que horas iniciaram as contrações", null=True, blank=True)
    duration_of_contractions = models.CharField(
        max_length=100, help_text="Duração das contrações", verbose_name="Duração das contrações", null=True, blank=True)
    interval_of_contractions = models.CharField(
        max_length=100, help_text="Intervalo das contrações", verbose_name="Intervalo das contrações", null=True, blank=True)
    pression_on_the_belly = models.BooleanField(
        help_text="Pressão na barriga", verbose_name="Pressão na barriga", null=True, blank=True)
    water_rupture = models.BooleanField(
        help_text="Rompimento da bolsa", verbose_name="Rompimento da bolsa", null=True, blank=True)
    visual_inspections = models.BooleanField(
        help_text="Inspeções visuais", verbose_name="Inspeções visuais", null=True, blank=True)
    birth_carried_out = models.BooleanField(
        help_text="Parto realizado", verbose_name="Parto realizado", null=True, blank=True)
    baby_sex = models.CharField(max_length=10, choices=SexType.choices,
                                help_text="Sexo do bebê", verbose_name="Sexo do bebê", null=True, blank=True)
    baby_name = models.CharField(
        max_length=100, help_text="Nome do bebê", verbose_name="Nome do bebê", null=True, blank=True)

    def __str__(self):
        return "Anamnsese Gestacional | " + self.gestational_period

    class Meta:
        verbose_name = "Anamnese Gestacional"
        verbose_name_plural = "Anamneses Gestacionais"


class Cinematic(BaseModel):
    behavior_desorder = models.BooleanField(
        help_text="Desordem de comportamento", verbose_name="Desordem de comportamento", null=True, blank=True)
    find_with_healmet = models.BooleanField(
        help_text="Encontrado com capacete", verbose_name="Encontrado com capacete", null=True, blank=True)
    find_with_seat_belt = models.BooleanField(
        help_text="Encontrado com cinto de segurança", verbose_name="Encontrado com cinto de segurança", null=True, blank=True)
    walking_in_the_cene = models.BooleanField(
        help_text="Caminhando na cena", verbose_name="Caminhando na cena", null=True, blank=True)
    broken_panel = models.BooleanField(
        help_text="Painel quebrado", verbose_name="Painel quebrado", null=True, blank=True)
    twisted_steering_wheel = models.BooleanField(
        help_text="Volante torcido", verbose_name="Volante torcido", null=True, blank=True)
    broken_windshield = models.BooleanField(
        help_text="Para-brisa quebrado", verbose_name="Para-brisa quebrado", null=True, blank=True)

    def __str__(self):
        return "Cinemática | " + str(self.id)

    class Meta:
        verbose_name = "Avaliação Cinemática"
        verbose_name_plural = "Avaliações Cinemáticas"


class DisposableMaterials(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Material descartável", verbose_name="Material descartável")
    size = models.CharField(max_length=100, choices=SizeType.choices, help_text="Tamanho",
                            verbose_name="Tamanho", null=True, blank=True)
    quantity = models.IntegerField(
        help_text="Quantidade", verbose_name="Quantidade", null=True, blank=True)
    disposable_materials_stock = models.ForeignKey(
        "DisposableMaterialsStock", on_delete=models.CASCADE, related_name='disposable_materials', blank=True, null=True, verbose_name="Estoque de materiais descartáveis")

    def __str__(self):
        return "Materiais Descartáveis | " + self.name

    def save(self, *args, **kwargs):
        if self.disposable_materials_stock and self.quantity:
            stock = self.disposable_materials_stock
            if stock.quantity >= self.quantity:
                stock.quantity -= self.quantity
                stock.save()
            else:
                raise ValidationError(
                    "Quantidade no estoque insuficiente para criar este material descartável.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Materiais Descartáveis"
        verbose_name_plural = "Materiais Descartáveis"


class DisposableMaterialsStock(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Material descartável", verbose_name="Material descartável")
    size = models.CharField(max_length=100, choices=SizeType.choices, help_text="Tamanho",
                            verbose_name="Tamanho", null=True, blank=True)
    quantity = models.IntegerField(
        help_text="Quantidade", verbose_name="Quantidade", null=True, blank=True)

    def __str__(self):
        return "Materiais Descartáveis em Estoque | " + self.name

    class Meta:
        verbose_name = "Materiais Descartáveis em Estoque"
        verbose_name_plural = "Materiais Descartáveis em Estoque"


class HospitalMaterials(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Material hospitalar", verbose_name="Material hospitalar")
    size = models.CharField(max_length=100, choices=SizeType.choices, help_text="Tamanho",
                            verbose_name="Tamanho", null=True, blank=True)
    quantity = models.IntegerField(
        help_text="Quantidade", verbose_name="Quantidade", null=True, blank=True)
    hospital_materials_stock = models.ForeignKey(
        "HospitalMaterialsStock", on_delete=models.CASCADE, related_name='hospital_materials', blank=True, null=True, verbose_name="Estoque de materiais hospitalares")

    def __str__(self):
        return "Material Hospitalar | " + self.name

    def save(self, *args, **kwargs):
        if self.hospital_materials_stock and self.quantity:
            stock = self.hospital_materials_stock
            if stock.quantity >= self.quantity:
                stock.quantity -= self.quantity
                stock.save()
            else:
                raise ValidationError(
                    "Quantidade no estoque insuficiente para criar este material hospitalar.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Material Hospitalar"
        verbose_name_plural = "Material Hospitalar"


class HospitalMaterialsStock(BaseModel):
    name = models.CharField(
        max_length=100, help_text="Material hospitalar", verbose_name="Material hospitalar")
    size = models.CharField(max_length=100, choices=SizeType.choices, help_text="Tamanho",
                            verbose_name="Tamanho", null=True, blank=True)
    quantity = models.IntegerField(
        help_text="Quantidade", verbose_name="Quantidade", null=True, blank=True)

    def __str__(self):
        return "Material Hospitalar em Estoque | " + self.name

    class Meta:
        verbose_name = "Material Hospitalar em Estoque"
        verbose_name_plural = "Material Hospitalar em Estoque"
