from apps.reports import api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("type_of_occurrence", api.TypeOfOccurrenceViewSet)
router.register("suspect_problems", api.SuspectProblemsViewSet)
router.register("signs_and_symptoms", api.SignsAndSymptomsViewSet)
router.register("glasgow", api.GlasgowViewSet)
router.register("glasgow-type", api.GlasgowTypeViewSet)
router.register("vital_signs", api.VitalSignsViewSet)
router.register("driving_style", api.DrivingStyleViewSet)
router.register("victim_was", api.VictimWasViewSet)
router.register("transport_decision", api.TransportDecisionViewSet)
router.register("service_team", api.ServiceTeamViewSet)
router.register("transport_informations", api.TransportInformationsViewSet)
router.register("proceeding", api.ProceedingViewSet)
router.register("anamnesis", api.AnamnesisViewSet)
router.register("gestacional_anamnesis", api.GestacionalAnamnesisViewSet)
router.register("cinematic", api.CinematicViewSet)
router.register("disposable_materials", api.DisposableMaterialsViewSet)
router.register("disposable_materials_stock",
                api.DisposableMaterialsStockViewSet)
router.register("hospital_materials", api.HospitalMaterialsViewSet)
router.register("hospital_materials_stock", api.HospitalMaterialsStockViewSet)
router.register("report", api.ReportViewSet)
router.register("report-register", api.ReportRegisterViewSet,
                basename="register-report")


urlpatterns = [
    path("", include(router.urls)),
]
