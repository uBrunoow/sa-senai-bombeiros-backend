from rest_framework import serializers
from .models import (
    TypeOfOccurrence,
    SuspectProblems,
    SignsAndSymptoms,
    GlasgowType,
    Glasgow,
    VitalSigns,
    DrivingStyle,
    VictimWas,
    TransportDecision,
    ServiceTeam,
    TransportInformations,
    Proceeding,
    Anamnesis,
    GestacionalAnamnesis,
    Cinematic,
    DisposableMaterials,
    HospitalMaterials,
    Report,
)

class TypeOfOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfOccurrence
        fields = "__all__"

class SuspectProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspectProblems
        fields = "__all__"

class SignsAndSymptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignsAndSymptoms
        fields = "__all__"
   
class GlasgowTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlasgowType
        fields = "__all__"
    
class GlasgowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glasgow
        fields = "__all__"

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSigns
        fields = "__all__"

class DrivingStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingStyle
        fields = "__all__"

class VictimWasSerializer(serializers.ModelSerializer):
    class Meta:
        model = VictimWas
        fields = "__all__"
    
class TransportDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportDecision
        fields = "__all__"

class ServiceTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTeam
        fields = "__all__"

class TransportInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportInformations
        fields = "__all__"

class ProceedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceeding
        fields = "__all__"

class AnamnesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnesis
        fields = "__all__"

class GestacionalAnamnesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestacionalAnamnesis
        fields = "__all__"

class CinematicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinematic
        fields = "__all__"

class DisposableMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisposableMaterials
        fields = "__all__"

class HospitalMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalMaterials
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

class ReportRegisterSerializer(serializers.ModelSerializer):
    glasgow = GlasgowSerializer(required=False)
    vital_signs = VitalSignsSerializer(required=False)
    service_team = ServiceTeamSerializer(required=False)
    transport_informations = TransportInformationsSerializer(required=False)
    anamnesis = AnamnesisSerializer(required=False)
    gestacional_anamnesis = GestacionalAnamnesisSerializer(required=False)
    cinematic = CinematicSerializer(required=False)

    class Meta:
        model = Report
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        glasgow_data = validated_data.pop("glasgow", None)
        vital_signs_data = validated_data.pop("vital_signs", None)
        service_team_data = validated_data.pop("service_team", None)
        transport_informations_data = validated_data.pop("transport_informations", None)
        anamnesis_data = validated_data.pop("anamnesis", None)
        gestacional_anamnesis_data = validated_data.pop("gestacional_anamnesis", None)
        cinematic_data = validated_data.pop("cinematic", None)

        glasgow = None
        vital_signs = None
        service_team = None
        transport_informations = None
        anamnesis = None
        gestacional_anamnesis = None
        cinematic = None

        # Valida e salva Glasgow, se presente
        if glasgow_data is not None:
            glasgow_serializer = GlasgowSerializer(data=glasgow_data)
            if glasgow_serializer.is_valid(raise_exception=True):
                glasgow = glasgow_serializer.save()

        # Valida e salva VitalSigns, se presente
        if vital_signs_data is not None:
            vital_signs_serializer = VitalSignsSerializer(data=vital_signs_data)
            if vital_signs_serializer.is_valid(raise_exception=True):
                vital_signs = vital_signs_serializer.save()

        if service_team_data is not None:
            service_team_serializer = ServiceTeamSerializer(data=service_team_data)
            if service_team_serializer.is_valid(raise_exception=True):
                service_team = service_team_serializer.save()

        if transport_informations_data is not None:
            transport_informations_serializer = TransportInformationsSerializer(data=transport_informations_data)
            if transport_informations_serializer.is_valid(raise_exception=True):
                transport_informations = transport_informations_serializer.save()

        if anamnesis_data is not None:
            anamnesis_serializer = AnamnesisSerializer(data=anamnesis_data)
            if anamnesis_serializer.is_valid(raise_exception=True):
                anamnesis = anamnesis_serializer.save()

        if gestacional_anamnesis_data is not None:
            gestacional_anamnesis_serializer = GestacionalAnamnesisSerializer(data=gestacional_anamnesis_data)
            if gestacional_anamnesis_serializer.is_valid(raise_exception=True):
                gestacional_anamnesis = gestacional_anamnesis_serializer.save()

        if cinematic_data is not None:
            cinematic_serializer = CinematicSerializer(data=cinematic_data)
            if cinematic_serializer.is_valid(raise_exception=True):
                cinematic = cinematic_serializer.save()

        # Cria o Report com os objetos Glasgow e VitalSigns associados
        report = Report.objects.create(
            glasgow=glasgow, 
            vital_signs=vital_signs,
            service_team=service_team,
            transport_informations=transport_informations,
            anamnesis=anamnesis,
            gestacional_anamnesis=gestacional_anamnesis,
            cinematic=cinematic,
            **validated_data
        )

        return report