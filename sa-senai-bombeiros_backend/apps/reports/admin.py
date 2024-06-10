from django.contrib.gis import admin
from django.contrib.auth.hashers import make_password
from apps.reports.models import (
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
    SubProblems,
    SubSubSignsAndSymptoms,
    SubSignsAndSymptoms,
    SubSubProceeding,
    SubProceeding,
)


class TypeOfOccurrenceAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
    
admin.site.register(TypeOfOccurrence, TypeOfOccurrenceAdmin)

class SubProblemAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
    
admin.site.register(SubProblems, SubProblemAdmin)

class SuspectProblemsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(SuspectProblems, SuspectProblemsAdmin)

class SubSubSignsAndSymptomsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(SubSubSignsAndSymptoms, SubSubSignsAndSymptomsAdmin)

class SubSignsAndSymptomsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(SubSignsAndSymptoms, SubSignsAndSymptomsAdmin)

class SignsAndSymptomsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(SignsAndSymptoms, SignsAndSymptomsAdmin)

class GlasgowTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "eye_opening" , "verbal_response", "motor_response","value" ,"created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(GlasgowType, GlasgowTypeAdmin)

class GlasgowAdmin(admin.ModelAdmin):
    list_display = ["eye_opening" , "verbal_response", "motor_response", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(Glasgow, GlasgowAdmin)

class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ["heart_rate" , "respiratory_rate", "blood_pressure", "temperature", "saturation","pulse", "perfusion_greater_than_two_seconds",  "perfusion_less_than_two_seconds", "is_normal" ,"created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(VitalSigns, VitalSignsAdmin)

class DrivingStyleAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(DrivingStyle, DrivingStyleAdmin)

class VictimWasAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
    search_fields = ["title"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(VictimWas, VictimWasAdmin)

class TransportDecisionAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(TransportDecision, TransportDecisionAdmin)

class ServiceTeamAdmin(admin.ModelAdmin):
    list_display = ["name_m", "name_s1", "name_s2", "name_s1", "name_demandante", "name_team" ,"created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(ServiceTeam, ServiceTeamAdmin)

class TransportInformationsAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(TransportInformations, TransportInformationsAdmin)

class SubSubProceedingAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(SubSubProceeding, SubSubProceedingAdmin)

class SubProceedingAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
    
admin.site.register(SubProceeding, SubProceedingAdmin)

class ProceedingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(Proceeding, ProceedingAdmin)

class AnamnesisAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(Anamnesis, AnamnesisAdmin)

class GestacionalAnamnesisAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(GestacionalAnamnesis, GestacionalAnamnesisAdmin)

class CinematicAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(Cinematic, CinematicAdmin)

class DisposableMaterialsAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(DisposableMaterials, DisposableMaterialsAdmin)

class HospitalMaterialsAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(HospitalMaterials, HospitalMaterialsAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(Report, ReportAdmin)