# Generated by Django 5.0.3 on 2024-03-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homs", "0018_alter_patient_patient_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="patient_id",
            field=models.CharField(editable=False, max_length=12, unique=True),
        ),
    ]
