from rest_framework import serializers
from ..management.serializers import UserReadOnlySerializer, FirefighterReadOnlySerializer
from .models import (
    TypeOfOccurrence,
    SuspectProblems,
    SubSuspectProblems,
    SignsAndSymptoms,
    SubSignsAndSymptoms,
    SubSubSignsAndSymptoms,
    GlasgowType,
    Glasgow,
    VitalSigns,
    DrivingStyle,
    VictimWas,
    TransportDecision,
    ServiceTeam,
    TransportInformations,
    Proceeding,
    SubProceeding,
    SubSubProceeding,
    Anamnesis,
    GestacionalAnamnesis,
    Cinematic,
    DisposableMaterials,
    DisposableMaterialsStock,
    HospitalMaterials,
    HospitalMaterialsStock,
    Report,
)


class TypeOfOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfOccurrence
        fields = ["id", "name"]


class SubSuspectProblemsSerializer(serializers.ModelSerializer):
    checked = serializers.SerializerMethodField()

    class Meta:
        model = SubSuspectProblems
        fields = ["id", "name", "checked"]

    def get_checked(self, obj):
        report = self.context.get('report')
        if report and report.sub_suspect_problems.filter(id=obj.id).exists():
            return True
        return False


class SuspectProblemsSerializer(serializers.ModelSerializer):
    sub_suspect_problems = serializers.SerializerMethodField()

    class Meta:
        model = SuspectProblems
        fields = ["id", "name", "sub_suspect_problems"]

    def get_sub_suspect_problems(self, obj):
        sub_suspect_problems = SubSuspectProblems.objects.filter(
            suspect_problem=obj)
        report = self.context.get('report')
        return SubSuspectProblemsSerializer(sub_suspect_problems, many=True, context={'report': report}).data


class SubSubSignsAndSymptomsSerializer(serializers.ModelSerializer):
    checked = serializers.SerializerMethodField()

    class Meta:
        model = SubSubSignsAndSymptoms
        fields = ["id", "name", "checked"]

    def get_checked(self, obj):
        report = self.context.get('report')
        if report and report.sub_sub_signs_and_symptoms.filter(id=obj.id).exists():
            return True
        return False


class SubSignsAndSymptomsSerializer(serializers.ModelSerializer):
    sub_sub_signs_and_symptoms = serializers.SerializerMethodField()
    checked = serializers.SerializerMethodField()

    class Meta:
        model = SubSignsAndSymptoms
        fields = ["id", "name", "sub_sub_signs_and_symptoms", "checked"]

    def get_sub_sub_signs_and_symptoms(self, obj):
        sub_sub_signs_and_symptoms = SubSubSignsAndSymptoms.objects.filter(
            sub_signs_and_symptoms=obj)
        report = self.context.get('report')
        return SubSubSignsAndSymptomsSerializer(sub_sub_signs_and_symptoms, many=True, context={'report': report}).data

    def get_checked(self, obj):
        report = self.context.get('report')
        if report and report.sub_signs_and_symptoms.filter(id=obj.id).exists():
            return True
        return False


class SignsAndSymptomsSerializer(serializers.ModelSerializer):
    sub_signs_and_symptoms = serializers.SerializerMethodField()

    class Meta:
        model = SignsAndSymptoms
        fields = ["id", "name", "sub_signs_and_symptoms"]

    def get_sub_signs_and_symptoms(self, obj):
        sub_signs_and_symptoms = SubSignsAndSymptoms.objects.filter(
            signs_and_symptoms=obj)
        report = self.context.get('report')
        return SubSignsAndSymptomsSerializer(sub_signs_and_symptoms, many=True, context={'report': report}).data


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
        fields = ["id", "name"]


class VictimWasSerializer(serializers.ModelSerializer):
    class Meta:
        model = VictimWas
        fields = ["id", "title"]


class TransportDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportDecision
        fields = ["id", "name"]


class ServiceTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTeam
        fields = "__all__"


class TransportInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportInformations
        fields = "__all__"


class SubSubProceedingSerializer(serializers.ModelSerializer):
    checked = serializers.SerializerMethodField()

    class Meta:
        model = SubSubProceeding
        fields = ["id", "name", "checked"]

    def get_checked(self, obj):
        report = self.context.get('report')
        if report and report.sub_sub_proceeding.filter(id=obj.id).exists():
            return True
        return False


class SubProceedingSerializer(serializers.ModelSerializer):
    sub_sub_proceeding = serializers.SerializerMethodField()
    checked = serializers.SerializerMethodField()

    class Meta:
        model = SubProceeding
        fields = ["id", "name", "sub_sub_proceeding", "checked"]

    def get_sub_sub_proceeding(self, obj):
        sub_sub_proceeding = SubSubProceeding.objects.filter(
            sub_proceeding=obj)
        report = self.context.get('report')
        return SubSubProceedingSerializer(sub_sub_proceeding, many=True, context={'report': report}).data

    def get_checked(self, obj):
        report = self.context.get('report')
        if report and report.sub_proceeding.filter(id=obj.id).exists():
            return True
        return False


class ProceedingSerializer(serializers.ModelSerializer):
    sub_proceeding = serializers.SerializerMethodField()

    class Meta:
        model = Proceeding
        fields = ["id", "name", "proceed_value", "sub_proceeding"]

    def get_sub_proceeding(self, obj):
        sub_proceeding = SubProceeding.objects.filter(proceeding=obj)
        report = self.context.get('report')
        return SubProceedingSerializer(sub_proceeding, many=True, context={'report': report}).data


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
    disposable_materials_stock = serializers.PrimaryKeyRelatedField(
        queryset=DisposableMaterialsStock.objects.all())

    class Meta:
        model = DisposableMaterials
        fields = "__all__"


class DisposableMaterialsStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisposableMaterialsStock
        fields = "__all__"


class HospitalMaterialsSerializer(serializers.ModelSerializer):
    hospital_materials_stock = serializers.PrimaryKeyRelatedField(
        queryset=HospitalMaterialsStock.objects.all())

    class Meta:
        model = HospitalMaterials
        fields = "__all__"


class HospitalMaterialsStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalMaterialsStock
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    type_of_occurrence = serializers.SerializerMethodField()
    suspect_problems = serializers.SerializerMethodField()
    signs_and_symptoms = serializers.SerializerMethodField()
    driving_style = serializers.SerializerMethodField()
    victim_was = serializers.SerializerMethodField()
    decision_transport = serializers.SerializerMethodField()
    proceeding = serializers.SerializerMethodField()
    disposable_materials = serializers.SerializerMethodField()
    hospital_materials = serializers.SerializerMethodField()
    user = UserReadOnlySerializer()
    glasgow = GlasgowSerializer()
    vital_signs = VitalSignsSerializer()
    service_team = ServiceTeamSerializer()
    transport_informations = TransportInformationsSerializer()
    anamnesis = AnamnesisSerializer()
    gestacional_anamnesis = GestacionalAnamnesisSerializer()
    cinematic = CinematicSerializer()

    class Meta:
        model = Report
        exclude = ["sub_suspect_problems", "sub_signs_and_symptoms",
                   "sub_sub_signs_and_symptoms", "sub_proceeding", "sub_sub_proceeding"]

    def get_type_of_occurrence(self, obj):
        return TypeOfOccurrenceSerializer(obj.type_of_occurrence.all(), many=True).data

    def get_suspect_problems(self, obj):
        return SuspectProblemsSerializer(obj.suspect_problems.all(), many=True, context={'report': obj}).data

    def get_signs_and_symptoms(self, obj):
        return SignsAndSymptomsSerializer(obj.signs_and_symptoms.all(), many=True, context={'report': obj}).data

    def get_driving_style(self, obj):
        return DrivingStyleSerializer(obj.driving_style.all(), many=True).data

    def get_victim_was(self, obj):
        return VictimWasSerializer(obj.victim_was.all(), many=True).data

    def get_decision_transport(self, obj):
        return TransportDecisionSerializer(obj.decision_transport.all(), many=True).data

    def get_proceeding(self, obj):
        return ProceedingSerializer(obj.proceeding.all(), many=True, context={'report': obj}).data

    def get_disposable_materials(self, obj):
        return DisposableMaterialsSerializer(obj.disposable_materials.all(), many=True).data

    def get_hospital_materials(self, obj):
        return HospitalMaterialsSerializer(obj.hospital_materials.all(), many=True).data


class ReportRegisterSerializer(serializers.ModelSerializer):
    type_of_occurrence = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TypeOfOccurrence.objects.all(), required=False
    )
    suspect_problems = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SuspectProblems.objects.all(), required=False
    )
    sub_suspect_problems = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SubSuspectProblems.objects.all(), required=False
    )
    signs_and_symptoms = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SignsAndSymptoms.objects.all(), required=False
    )
    sub_signs_and_symptoms = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SubSignsAndSymptoms.objects.all(), required=False
    )
    sub_sub_signs_and_symptoms = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SubSubSignsAndSymptoms.objects.all(), required=False
    )
    driving_style = serializers.PrimaryKeyRelatedField(
        many=True, queryset=DrivingStyle.objects.all(), required=False
    )
    victim_was = serializers.PrimaryKeyRelatedField(
        many=True, queryset=VictimWas.objects.all(), required=False
    )
    decision_transport = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TransportDecision.objects.all(), required=False
    )
    proceeding = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Proceeding.objects.all(), required=False
    )
    sub_proceeding = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SubProceeding.objects.all(), required=False
    )
    sub_sub_proceeding = serializers.PrimaryKeyRelatedField(
        many=True, queryset=SubSubProceeding.objects.all(), required=False
    )
    disposable_materials = DisposableMaterialsSerializer(
        many=True, required=False)
    hospital_materials = HospitalMaterialsSerializer(many=True, required=False)
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
        type_of_occurrence_data = validated_data.pop('type_of_occurrence', [])
        suspect_problems_data = validated_data.pop('suspect_problems', [])
        sub_suspect_problems_data = validated_data.pop(
            'sub_suspect_problems', [])
        signs_and_symptoms_data = validated_data.pop('signs_and_symptoms', [])
        sub_signs_and_symptoms_data = validated_data.pop(
            'sub_signs_and_symptoms', [])
        sub_sub_signs_and_symptoms_data = validated_data.pop(
            'sub_sub_signs_and_symptoms', [])
        driving_style_data = validated_data.pop('driving_style', [])
        victim_was_data = validated_data.pop('victim_was', [])
        decision_transport_data = validated_data.pop('decision_transport', [])
        proceeding_data = validated_data.pop('proceeding', [])
        sub_proceeding_data = validated_data.pop('sub_proceeding', [])
        sub_sub_proceeding_data = validated_data.pop('sub_sub_proceeding', [])
        disposable_materials_data = validated_data.pop(
            'disposable_materials', [])
        hospital_materials_data = validated_data.pop('hospital_materials', [])

        glasgow_data = validated_data.pop('glasgow', None)
        vital_signs_data = validated_data.pop('vital_signs', None)
        service_team_data = validated_data.pop('service_team', None)
        transport_informations_data = validated_data.pop(
            'transport_informations', None)
        anamnesis_data = validated_data.pop('anamnesis', None)
        gestacional_anamnesis_data = validated_data.pop(
            'gestacional_anamnesis', None)
        cinematic_data = validated_data.pop('cinematic', None)

        if glasgow_data:
            glasgow_instance = Glasgow.objects.create(**glasgow_data)
            validated_data['glasgow'] = glasgow_instance

        if vital_signs_data:
            vital_signs_instance = VitalSigns.objects.create(
                **vital_signs_data)
            validated_data['vital_signs'] = vital_signs_instance

        if service_team_data:
            service_team_instance = ServiceTeam.objects.create(
                **service_team_data)
            validated_data['service_team'] = service_team_instance

        if transport_informations_data:
            transport_informations_instance = TransportInformations.objects.create(
                **transport_informations_data)
            validated_data['transport_informations'] = transport_informations_instance

        if anamnesis_data:
            anamnesis_instance = Anamnesis.objects.create(**anamnesis_data)
            validated_data['anamnesis'] = anamnesis_instance

        if gestacional_anamnesis_data:
            gestacional_anamnesis_instance = GestacionalAnamnesis.objects.create(
                **gestacional_anamnesis_data)
            validated_data['gestacional_anamnesis'] = gestacional_anamnesis_instance

        if cinematic_data:
            cinematic_instance = Cinematic.objects.create(**cinematic_data)
            validated_data['cinematic'] = cinematic_instance

        report = Report.objects.create(**validated_data)

        report.type_of_occurrence.set(type_of_occurrence_data)
        report.suspect_problems.set(suspect_problems_data)
        report.sub_suspect_problems.set(sub_suspect_problems_data)
        report.signs_and_symptoms.set(signs_and_symptoms_data)
        report.sub_signs_and_symptoms.set(sub_signs_and_symptoms_data)
        report.sub_sub_signs_and_symptoms.set(sub_sub_signs_and_symptoms_data)
        report.driving_style.set(driving_style_data)
        report.victim_was.set(victim_was_data)
        report.decision_transport.set(decision_transport_data)
        report.proceeding.set(proceeding_data)
        report.sub_proceeding.set(sub_proceeding_data)
        report.sub_sub_proceeding.set(sub_sub_proceeding_data)

        for disposable_material_data in disposable_materials_data:
            disposable_material_instance = DisposableMaterials.objects.create(
                **disposable_material_data)
            report.disposable_materials.add(disposable_material_instance)

            stock = disposable_material_data.get('disposable_materials_stock')
            quantity = disposable_material_instance.quantity

            if stock and quantity:
                if stock.quantity >= quantity:
                    stock.quantity -= quantity
                    stock.save()
                else:
                    raise serializers.ValidationError(
                        "Quantidade no estoque insuficiente para criar este material descartável.")

        for hospital_material_data in hospital_materials_data:
            hospital_material_instance = HospitalMaterials.objects.create(
                **hospital_material_data)
            report.hospital_materials.add(hospital_material_instance)

            stock = hospital_material_data.get('hospital_materials_stock')
            quantity = hospital_material_instance.quantity

            if stock and quantity:
                if stock.quantity >= quantity:
                    stock.quantity -= quantity
                    stock.save()
                else:
                    raise serializers.ValidationError(
                        "Quantidade no estoque insuficiente para criar este material descartável.")

        return report
