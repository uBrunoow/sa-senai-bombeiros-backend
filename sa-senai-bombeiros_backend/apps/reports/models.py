import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from django.conf import settings
from apps.management.models import User

class TypeOfOccurrence(BaseModel):
    name = models.CharField(max_length=100, help_text="Tipo de ocorrência", verbose_name="Tipo de ocorrência")

    def __str__(self):
        return self.name
    
class SubProblems(BaseModel):
    name = models.CharField(max_length=100, help_text="Problema", verbose_name="Problema")
    
    def __str__(self):
        return self.name

class SuspectProblems(BaseModel):
    name = models.CharField(max_length=100, help_text="Problema do suspeito", verbose_name="Problema do suspeito")
    sub_problems = models.ManyToManyField('SubProblems', related_name='child_problems', blank=True)  # Corrected related_name

    def __str__(self):
        return self.name

    
class SubSubSignsAndSymptoms(BaseModel):
    name = models.CharField(max_length=100, help_text="Sinais e sintomas", verbose_name="Sinais e sintomas")

    def __str__(self):
        return self.name

class SubSignsAndSymptoms(BaseModel):
    name = models.CharField(max_length=100, help_text="Sinais e sintomas", verbose_name="Sinais e sintomas")
    sub_sub_symptoms = models.ManyToManyField('SubSubSignsAndSymptoms', related_name='child_sub_symptoms', blank=True)  # Corrected related_name

    def __str__(self):
        return self.name

class SignsAndSymptoms(BaseModel):
    name = models.CharField(max_length=100, help_text="Sinais e sintomas", verbose_name="Sinais e sintomas")
    sub_symptoms = models.ManyToManyField('SubSignsAndSymptoms', related_name='child_child_sub_symptoms', blank=True)

    def __str__(self):
        return self.name

class GlasgowType(BaseModel):
    name = models.CharField(max_length=100, help_text="Tipo de Glasgow", verbose_name="Tipo de Glasgow", null=True, blank=True)
    grater_than_five_year = models.BooleanField(help_text="Maior que cinco anos", verbose_name="Maior que cinco anos", null=True, blank=True)
    less_than_five_year = models.BooleanField(help_text="Menor que cinco anos", verbose_name="Menor que cinco anos", null=True, blank=True)
    eye_opening = models.BooleanField(help_text="Abertura ocular", verbose_name="Abertura ocular", null=True, blank=True)
    verbal_response = models.BooleanField(help_text="Resposta verbal", verbose_name="Resposta verbal", null=True, blank=True)
    motor_response = models.BooleanField(help_text="Resposta motora", verbose_name="Resposta motora", null=True, blank=True)
    value = models.IntegerField(help_text="Valor", verbose_name="Valor", null=True, blank=True)

    def __str__(self):
        return self.name

class Glasgow(BaseModel):
    eye_opening = models.IntegerField(help_text="Abertura ocular", verbose_name="Abertura ocular", null=True, blank=True)
    verbal_response = models.IntegerField(help_text="Resposta verbal", verbose_name="Resposta verbal", null=True, blank=True)
    motor_response = models.IntegerField(help_text="Resposta motora", verbose_name="Resposta motora", null=True, blank=True)
    total = models.IntegerField(help_text="Total", verbose_name="Total", null=True, blank=True)

    def __str__(self):
        return 'Total foi de ' + str(self.total)

class VitalSigns(BaseModel):
    heart_rate = models.IntegerField(help_text="Frequência cardíaca", verbose_name="Frequência cardíaca", null=True, blank=True)
    respiratory_rate = models.IntegerField(help_text="Frequência respiratória", verbose_name="Frequência respiratória", null=True, blank=True)
    blood_pressure = models.IntegerField(help_text="Pressão arterial", verbose_name="Pressão arterial", null=True, blank=True)
    temperature = models.IntegerField(help_text="Temperatura", verbose_name="Temperatura", null=True, blank=True)
    saturation = models.IntegerField(help_text="Saturação", verbose_name="Saturação", null=True, blank=True)
    pulse = models.IntegerField(help_text="Pulso", verbose_name="Pulso", null=True, blank=True)
    perfusion_greater_than_two_seconds = models.BooleanField(help_text="Perfusão maior que dois segundos", verbose_name="Perfusão maior que dois segundos", null=True, blank=True)
    perfusion_less_than_two_seconds = models.BooleanField(help_text="Perfusão menor que dois segundos", verbose_name="Perfusão menor que dois segundos", null=True, blank=True)
    is_normal = models.BooleanField(help_text="Normal", verbose_name="Normal", null=True, blank=True)

    def __str__(self):
        return str(self.heart_rate)
    
class DrivingStyle(BaseModel):
    name = models.CharField(max_length=100, help_text="Estilo de direção", verbose_name="Estilo de direção")

    def __str__(self):
        return self.name
    
class VictimWas(BaseModel):
    title = models.CharField(max_length=100, help_text="Título", verbose_name="Título")

    def __str__(self):
        return self.title

class TransportDecision(BaseModel):
    name = models.CharField(max_length=100, help_text="Decisão de transporte", verbose_name="Decisão de transporte")

    def __str__(self):
        return self.name
    
class ServiceTeam(BaseModel):
    name_m = models.CharField(max_length=100, help_text="M", verbose_name="M", null=True, blank=True)
    name_s1 = models.CharField(max_length=100, help_text="S1", verbose_name="S1", null=True, blank=True)
    name_s2 = models.CharField(max_length=100, help_text="S2", verbose_name="S2", null=True, blank=True)
    name_demandante = models.CharField(max_length=100, help_text="Demandante", verbose_name="Demandante", null=True, blank=True)
    name_team = models.CharField(max_length=100, help_text="Equipe", verbose_name="Equipe", null=True, blank=True)

    def __str__(self):
        return self.name_team
    
class TransportInformations(BaseModel):
    number_usb = models.IntegerField(help_text="Número USB", verbose_name="Número USB", null=True, blank=True)
    num_occurencies = models.IntegerField(help_text="Número de ocorrências", verbose_name="Número de ocorrências", null=True, blank=True)
    desp = models.CharField(max_length=100, help_text="Despachante", verbose_name="Despachante", null=True, blank=True)
    ir_cod = models.BooleanField(help_text="Código IR", verbose_name="Código IR", null=True, blank=True)
    ps_cod = models.BooleanField(help_text="Código PS", verbose_name="Código PS", null=True, blank=True)
    sia_sus_cod = models.BooleanField(help_text="Código SIA/SUS", verbose_name="Código SIA/SUS", null=True, blank=True)
    final_km = models.IntegerField(help_text="KM final", verbose_name="KM final", null=True, blank=True)
    hch = models.CharField(max_length=100, help_text="HCH", verbose_name="HCH", null=True, blank=True)

class SubSubProceeding(BaseModel):
    name = models.CharField(max_length=100, help_text="Procedimento", verbose_name="Procedimento")
    
    def __str__(self):
        return self.name
    
class SubProceeding(BaseModel):
    name = models.CharField(max_length=100, help_text="Procedimento", verbose_name="Procedimento")
    sub_sub_proceed = models.ManyToManyField('SubSubProceeding', related_name='child_sub_proceedings', blank=True)  # Corrected related_name

    def __str__(self):
        return self.name

class Proceeding(BaseModel):
    name = models.CharField(max_length=100, help_text="Procedimento", verbose_name="Procedimento")
    sub_proceed = models.ManyToManyField('SubProceeding', related_name='child_proceedings')  # Corrected related_name
    proceed_value = models.IntegerField(help_text="Valor", verbose_name="Valor", null=True, blank=True)
    
    def __str__(self):
        return self.name

class Anamnesis(BaseModel):
    what_happend = models.TextField(help_text="O que aconteceu", verbose_name="O que aconteceu", null=True, blank=True)
    happend_other_times = models.BooleanField(help_text="Aconteceu outras vezes", verbose_name="Aconteceu outras vezes", null=True, blank=True)
    how_long_happend = models.CharField(max_length=100, help_text="Quanto tempo aconteceu", verbose_name="Quanto tempo aconteceu", null=True, blank=True)
    health_problems = models.BooleanField(help_text="Problemas de saúde", verbose_name="Problemas de saúde", null=True, blank=True)
    health_problems_description = models.TextField(help_text="Descrição de problemas de saúde", verbose_name="Descrição de problemas de saúde", null=True, blank=True)
    alergies = models.BooleanField(help_text="Alergias", verbose_name="Alergias", null=True, blank=True)
    alergies_description = models.TextField(help_text="Descrição de alergias", verbose_name="Descrição de alergias", null=True, blank=True)
    medications = models.BooleanField(help_text="Medicamentos", verbose_name="Medicamentos", null=True, blank=True)
    medications_description = models.TextField(help_text="Descrição de medicamentos", verbose_name="Descrição de medicamentos", null=True, blank=True)
    hour_of_last_medication = models.CharField(max_length=100, help_text="Hora da última medicação", verbose_name="Hora da última medicação", null=True, blank=True)
    drank_liquid_food = models.BooleanField(help_text="Líquidos e alimentos ingeridos", verbose_name="Líquidos e alimentos ingeridos", null=True, blank=True)
    hour_of_last_drank_liquid_food = models.CharField(max_length=100, help_text="Hora da última ingestão de líquidos e alimentos", verbose_name="Hora da última ingestão de líquidos e alimentos", null=True, blank=True)

    def __str__(self):
        return self.what_happend
    
class SexType(models.TextChoices):
    MALE = 'MALE', 'Masculino'
    FEMALE = 'FEMALE', 'Feminino'

class GestacionalAnamnesis(BaseModel):
    gestational_period = models.CharField(max_length=100, help_text="Período gestacional", verbose_name="Período gestacional", null=True, blank=True)
    pre_natal = models.BooleanField(help_text="Pré-natal", verbose_name="Pré-natal", null=True, blank=True)
    complications = models.BooleanField(help_text="Complicações", verbose_name="Complicações", null=True, blank=True)
    first_child = models.BooleanField(help_text="Primeira gestação", verbose_name="Primeira gestação", null=True, blank=True)
    number_of_children = models.IntegerField(help_text="Número de filhos", verbose_name="Número de filhos", null=True, blank=True)
    time_of_contractions = models.CharField(max_length=100, help_text="Que horas iniciaram as contrações", verbose_name="Que horas iniciaram as contrações", null=True, blank=True)
    duration_of_contractions = models.CharField(max_length=100, help_text="Duração das contrações", verbose_name="Duração das contrações", null=True, blank=True)
    interval_of_contractions = models.CharField(max_length=100, help_text="Intervalo das contrações", verbose_name="Intervalo das contrações", null=True, blank=True)
    pression_on_the_belly = models.BooleanField(help_text="Pressão na barriga", verbose_name="Pressão na barriga", null=True, blank=True)
    water_rupture = models.BooleanField(help_text="Rompimento da bolsa", verbose_name="Rompimento da bolsa", null=True, blank=True)
    visual_inspections = models.BooleanField(help_text="Inspeções visuais", verbose_name="Inspeções visuais", null=True, blank=True)
    birth_carried_out = models.BooleanField(help_text="Parto realizado", verbose_name="Parto realizado", null=True, blank=True)
    baby_sex = models.CharField(max_length=10, choices=SexType.choices, help_text="Sexo do bebê", verbose_name="Sexo do bebê", null=True, blank=True)
    baby_name = models.CharField(max_length=100, help_text="Nome do bebê", verbose_name="Nome do bebê", null=True, blank=True)

    def __str__(self):
        return self.gestational_period
    
class Cinematic(BaseModel):
    behavior_desorder = models.BooleanField(help_text="Desordem de comportamento", verbose_name="Desordem de comportamento", null=True, blank=True)
    find_with_healmet = models.BooleanField(help_text="Encontrado com capacete", verbose_name="Encontrado com capacete", null=True, blank=True)
    find_with_seat_belt = models.BooleanField(help_text="Encontrado com cinto de segurança", verbose_name="Encontrado com cinto de segurança", null=True, blank=True)
    walking_in_the_cene = models.BooleanField(help_text="Caminhando na cena", verbose_name="Caminhando na cena", null=True, blank=True)
    broken_panel = models.BooleanField(help_text="Painel quebrado", verbose_name="Painel quebrado", null=True, blank=True)
    twisted_steering_wheel = models.BooleanField(help_text="Volante torcido", verbose_name="Volante torcido", null=True, blank=True)
    broken_windshield = models.BooleanField(help_text="Para-brisa quebrado", verbose_name="Para-brisa quebrado", null=True, blank=True)

    def __str__(self):
        return "Cinemática" + str(self.behavior_desorder)

class DisposableMaterials(BaseModel):
    name = models.CharField(max_length=100, help_text="Material descartável", verbose_name="Material descartável")
    size = models.CharField(max_length=100, help_text="Tamanho", verbose_name="Tamanho", null=True, blank=True)
    quantity = models.IntegerField(help_text="Quantidade", verbose_name="Quantidade", null=True, blank=True)

    def __str__(self):
        return self.name

class HospitalMaterials(BaseModel):
    name = models.CharField(max_length=100, help_text="Material hospitalar", verbose_name="Material hospitalar")
    size = models.CharField(max_length=100, help_text="Tamanho", verbose_name="Tamanho", null=True, blank=True)
    quantity = models.IntegerField(help_text="Quantidade", verbose_name="Quantidade", null=True, blank=True)

    def __str__(self):
        return self.name

class Report(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')
    report_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100, help_text="Nome da vítima", verbose_name="Nome", null=True, blank=True)
    general_registration = models.CharField(max_length=100, help_text="Registro geral", verbose_name="Registro geral", null=True, blank=True)
    age = models.IntegerField(help_text="Idade da vítima", verbose_name="Idade", null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SexType.choices, help_text="Sexo", verbose_name="Sexo", null=True, blank=True)
    escort = models.CharField(max_length=100, help_text="Acompanhante", verbose_name="Acompanhante", null=True, blank=True)
    escort_age = models.IntegerField(help_text="Idade do acompanhante", verbose_name="Idade do acompanhante", null=True, blank=True)
    report_place = models.CharField(max_length=100, help_text="Local do acidente", verbose_name="Local do acidente", null=True, blank=True)
    phone = models.CharField(max_length=100, help_text="Telefone para contato", verbose_name="Telefone para contato", null=True, blank=True)
    type_of_occurrences = models.ManyToManyField(TypeOfOccurrence, related_name='reports', blank=True)
    other_occurrence = models.TextField(help_text="Descrição para outros tipos de ocorrências", verbose_name="Outro", null=True, blank=True)
    suspect_problems = models.ManyToManyField(SuspectProblems, related_name='reports', blank=True)
    other_problems = models.TextField(help_text="Descrição para outros problemas", verbose_name="Outro", null=True, blank=True)
    signs_and_symptoms = models.ManyToManyField(SignsAndSymptoms, related_name='reports', blank=True)
    other_signs_and_symptoms = models.TextField(help_text="Descrição para outros sinais e sintomas", verbose_name="Outro", null=True, blank=True)
    glasgow = models.ForeignKey(Glasgow, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    vital_signs = models.ForeignKey(VitalSigns, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    driving_style = models.ManyToManyField(DrivingStyle, related_name='reports', blank=True)
    victim_was = models.ManyToManyField(VictimWas, related_name='reports', blank=True)
    decision_transport = models.ManyToManyField(TransportDecision, related_name='reports', blank=True)
    service_team = models.ForeignKey(ServiceTeam, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    objects_recovered = models.TextField(help_text="Objetos recuperados", verbose_name="Objetos recuperados", null=True, blank=True)
    transport_informations = models.ForeignKey(TransportInformations, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    proceeding = models.ManyToManyField(Proceeding, related_name='reports', blank=True)
    other_proceeding = models.TextField(help_text="Descrição para outros procedimentos", verbose_name="Outro", null=True, blank=True)
    observations = models.TextField(help_text="Observações", verbose_name="Observações", null=True, blank=True)
    anamnesis = models.ForeignKey(Anamnesis, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    gestacional_anamnesis = models.ForeignKey(GestacionalAnamnesis, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    cinematic = models.ForeignKey(Cinematic, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    disposable_materials = models.ManyToManyField(DisposableMaterials, related_name='reports', blank=True)
    other_disposable_materials = models.TextField(help_text="Descrição para outros materiais descartáveis", verbose_name="Outro", null=True, blank=True)
    quantity_other_disposable_materials = models.IntegerField(help_text="Quantidade de outros materiais descartáveis", verbose_name="Quantidade de outros materiais descartáveis", null=True, blank=True)
    hospital_materials = models.ManyToManyField(HospitalMaterials, related_name='reports', blank=True)
    other_hospital_materials = models.TextField(help_text="Descrição para outros materiais hospitalares", verbose_name="Outro", null=True, blank=True)
    quantity_other_materials = models.IntegerField(help_text="Quantidade de outros materiais hospitalares", verbose_name="Quantidade de outros materiais hospitalares", null=True, blank=True)
    responsable_for_report = models.CharField(max_length=100, help_text="Responsável pelo relatório", verbose_name="Responsável pelo relatório", null=True, blank=True)

    def __str__(self):
        return self.name