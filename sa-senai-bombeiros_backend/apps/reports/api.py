from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import BlacklistedToken, OutstandingToken
from rest_framework.response import Response
from rest_framework import (
    generics,
    mixins,
    permissions,
    response,
    status,
    views,
    viewsets,
)
from utils.actions import DRFAction
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
from .serializers import (
    TypeOfOccurrenceSerializer,
    SuspectProblemsSerializer,
    SignsAndSymptomsSerializer,
    GlasgowTypeSerializer,
    GlasgowSerializer,
    VitalSignsSerializer,
    DrivingStyleSerializer,
    VictimWasSerializer,
    TransportDecisionSerializer,
    ServiceTeamSerializer,
    TransportInformationsSerializer,
    ProceedingSerializer,
    AnamnesisSerializer,
    GestacionalAnamnesisSerializer,
    CinematicSerializer,
    DisposableMaterialsSerializer,
    HospitalMaterialsSerializer,
    ReportSerializer,
    ReportRegisterSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters

class TypeOfOccurrenceViewSet(viewsets.ModelViewSet):
    queryset = TypeOfOccurrence.objects.all()
    serializer_class = TypeOfOccurrenceSerializer

class SuspectProblemsViewSet(viewsets.ModelViewSet):
    queryset = SuspectProblems.objects.all()
    serializer_class = SuspectProblemsSerializer

class SignsAndSymptomsViewSet(viewsets.ModelViewSet):
    queryset = SignsAndSymptoms.objects.all()
    serializer_class = SignsAndSymptomsSerializer

class GlasgowTypeViewSet(viewsets.ModelViewSet):
    queryset = GlasgowType.objects.all()
    serializer_class = GlasgowTypeSerializer

class GlasgowViewSet(viewsets.ModelViewSet):
    queryset = Glasgow.objects.all()
    serializer_class = GlasgowSerializer

class VitalSignsViewSet(viewsets.ModelViewSet):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializer

class DrivingStyleViewSet(viewsets.ModelViewSet):
    queryset = DrivingStyle.objects.all()
    serializer_class = DrivingStyleSerializer

class VictimWasViewSet(viewsets.ModelViewSet):
    queryset = VictimWas.objects.all()
    serializer_class = VictimWasSerializer

class TransportDecisionViewSet(viewsets.ModelViewSet):
    queryset = TransportDecision.objects.all()
    serializer_class = TransportDecisionSerializer

class ServiceTeamViewSet(viewsets.ModelViewSet):
    queryset = ServiceTeam.objects.all()
    serializer_class = ServiceTeamSerializer

class TransportInformationsViewSet(viewsets.ModelViewSet):
    queryset = TransportInformations.objects.all()
    serializer_class = TransportInformationsSerializer

class ProceedingViewSet(viewsets.ModelViewSet):
    queryset = Proceeding.objects.all()
    serializer_class = ProceedingSerializer

class AnamnesisViewSet(viewsets.ModelViewSet):
    queryset = Anamnesis.objects.all()
    serializer_class = AnamnesisSerializer

class GestacionalAnamnesisViewSet(viewsets.ModelViewSet):
    queryset = GestacionalAnamnesis.objects.all()
    serializer_class = GestacionalAnamnesisSerializer

class CinematicViewSet(viewsets.ModelViewSet):
    queryset = Cinematic.objects.all()
    serializer_class = CinematicSerializer

class DisposableMaterialsViewSet(viewsets.ModelViewSet):
    queryset = DisposableMaterials.objects.all()
    serializer_class = DisposableMaterialsSerializer

class HospitalMaterialsViewSet(viewsets.ModelViewSet):
    queryset = HospitalMaterials.objects.all()
    serializer_class = HospitalMaterialsSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportRegisterViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ReportRegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.none()

    def perform_create(self, serializer):
        res = super().perform_create(serializer)
        return res