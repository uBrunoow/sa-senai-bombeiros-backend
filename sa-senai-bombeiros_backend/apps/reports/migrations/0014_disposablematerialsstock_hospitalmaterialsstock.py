# Generated by Django 4.2.6 on 2024-07-31 22:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0013_alter_anamnesis_options_alter_cinematic_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DisposableMaterialsStock",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Material descartável",
                        max_length=100,
                        verbose_name="Material descartável",
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("8", "8"),
                            ("12", "12"),
                            ("20", "20"),
                            ("H", "H"),
                            ("P", "P"),
                            ("O", "O"),
                            ("G", "G"),
                            ("N", "N"),
                            ("PP", "PP"),
                            ("M", "M"),
                            ("ADULTO", "ADULTO"),
                            ("INFANTIL", "INFANTIL"),
                        ],
                        help_text="Tamanho",
                        max_length=100,
                        null=True,
                        verbose_name="Tamanho",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        blank=True,
                        help_text="Quantidade",
                        null=True,
                        verbose_name="Quantidade",
                    ),
                ),
            ],
            options={
                "verbose_name": "Materiais Descartáveis em Estoque",
                "verbose_name_plural": "Materiais Descartáveis em Estoque",
            },
        ),
        migrations.CreateModel(
            name="HospitalMaterialsStock",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Material hospitalar",
                        max_length=100,
                        verbose_name="Material hospitalar",
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("8", "8"),
                            ("12", "12"),
                            ("20", "20"),
                            ("H", "H"),
                            ("P", "P"),
                            ("O", "O"),
                            ("G", "G"),
                            ("N", "N"),
                            ("PP", "PP"),
                            ("M", "M"),
                            ("ADULTO", "ADULTO"),
                            ("INFANTIL", "INFANTIL"),
                        ],
                        help_text="Tamanho",
                        max_length=100,
                        null=True,
                        verbose_name="Tamanho",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        blank=True,
                        help_text="Quantidade",
                        null=True,
                        verbose_name="Quantidade",
                    ),
                ),
            ],
            options={
                "verbose_name": "Material Hospitalar em Estoque",
                "verbose_name_plural": "Material Hospitalar em Estoque",
            },
        ),
    ]
