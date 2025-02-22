# Generated by Django 4.2.6 on 2024-07-31 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "reports",
            "0015_disposablematerialsstock_disposable_materials_stock_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="disposablematerialsstock",
            name="disposable_materials_stock",
        ),
        migrations.AddField(
            model_name="disposablematerials",
            name="disposable_materials_stock",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="disposable_materials",
                to="reports.disposablematerialsstock",
                verbose_name="Estoque de materiais descartáveis",
            ),
        ),
    ]
