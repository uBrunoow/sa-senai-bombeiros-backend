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
    DisposableMaterialsStock,
    HospitalMaterials,
    HospitalMaterialsStock,
    Report,
    SubSuspectProblems,
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
    list_display = ["name", "suspect_problem", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SubSuspectProblems, SubProblemAdmin)


class SuspectProblemsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SuspectProblems, SuspectProblemsAdmin)


class SubSubSignsAndSymptomsAdmin(admin.ModelAdmin):
    list_display = ["name", "sub_signs_and_symptoms",
                    "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SubSubSignsAndSymptoms, SubSubSignsAndSymptomsAdmin)


class SubSignsAndSymptomsAdmin(admin.ModelAdmin):
    list_display = ["name", "signs_and_symptoms", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SubSignsAndSymptoms, SubSignsAndSymptomsAdmin)


class SignsAndSymptomsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SignsAndSymptoms, SignsAndSymptomsAdmin)


class SubSubProceedingAdmin(admin.ModelAdmin):
    list_display = ["name", "sub_proceeding", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SubSubProceeding, SubSubProceedingAdmin)


class SubProceedingAdmin(admin.ModelAdmin):
    list_display = ["name", "proceeding", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(SubProceeding, SubProceedingAdmin)


class ProceedingAdmin(admin.ModelAdmin):
    list_display = ["name", "proceed_value", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(Proceeding, ProceedingAdmin)


class GlasgowTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "eye_opening", "is_grater_than_five_year", "verbal_response",
                    "motor_response", "value", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(GlasgowType, GlasgowTypeAdmin)


class GlasgowAdmin(admin.ModelAdmin):
    list_display = ["eye_opening", "verbal_response",
                    "motor_response", "total", "total_score", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    readonly_fields = ["total"]

    def total_score(self, obj):
        return obj.eye_opening + obj.verbal_response + obj.motor_response
    total_score.short_description = "Total Score"


admin.site.register(Glasgow, GlasgowAdmin)


class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ["heart_rate", "respiratory_rate", "blood_pressure", "temperature", "saturation", "pulse",
                    "perfusion_is_greater_than_two_seconds", "is_normal", "created_at", "updated_at"]
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
    list_display = ["name_m", "name_s1", "name_s2", "name_s1",
                    "name_demandante", "name_team", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(ServiceTeam, ServiceTeamAdmin)


class TransportInformationsAdmin(admin.ModelAdmin):
    list_display = ["number_usb", "num_occurencies", "desp", "ir_cod",
                    "ps_cod", "sia_sus_cod", "final_km", "hch",   "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(TransportInformations, TransportInformationsAdmin)


class AnamnesisAdmin(admin.ModelAdmin):
    list_display = ["what_happend", "happend_other_times",
                    "how_long_happend", "health_problems",
                    "health_problems_description", "alergies",
                    "alergies_description", "medications",
                    "medications_description", "hour_of_last_medication",
                    "drank_liquid_food", "hour_of_last_drank_liquid_food",
                    "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(Anamnesis, AnamnesisAdmin)


class GestacionalAnamnesisAdmin(admin.ModelAdmin):
    list_display = [
        "gestational_period", "pre_natal", "complications",
        "first_child", "number_of_children", "time_of_contractions",
        "duration_of_contractions", "interval_of_contractions",
        "pression_on_the_belly", "water_rupture",
        "visual_inspections", "birth_carried_out",
        "baby_sex", "baby_name",
        "created_at", "updated_at"
    ]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(GestacionalAnamnesis, GestacionalAnamnesisAdmin)


class CinematicAdmin(admin.ModelAdmin):
    list_display = [
        "behavior_desorder", "find_with_healmet",
        "find_with_seat_belt", "walking_in_the_cene",
        "broken_panel", "twisted_steering_wheel", "broken_windshield",
        "created_at", "updated_at"
    ]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(Cinematic, CinematicAdmin)


class DisposableMaterialsAdmin(admin.ModelAdmin):
    list_display = ["name", "size", "quantity", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(DisposableMaterials, DisposableMaterialsAdmin)


class DisposableMaterialsStockAdmin(admin.ModelAdmin):
    list_display = ["name", "size", "quantity", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(DisposableMaterialsStock, DisposableMaterialsStockAdmin)


class HospitalMaterialsAdmin(admin.ModelAdmin):
    list_display = ["name", "size", "quantity", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(HospitalMaterials, HospitalMaterialsAdmin)


class HospitalMaterialsStockAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity",  "size", "created_at", "updated_at"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(HospitalMaterialsStock, HospitalMaterialsStockAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "user",
        "general_registration",
        "age",
        "sex",
        "report_date",
        "created_at",
        "updated_at"
    ]
    list_filter = ["created_at", "updated_at"]


admin.site.register(Report, ReportAdmin)
