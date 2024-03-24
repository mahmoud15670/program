# Generated by Django 5.0.3 on 2024-03-24 13:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("homs", "0015_remove_result_patient_remove_result_test_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("age", models.PositiveSmallIntegerField()),
                (
                    "date",
                    models.CharField(
                        choices=[("year", "year"), ("month", "month"), ("day", "day")],
                        max_length=5,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")], max_length=6
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=12)),
                ("dr", models.CharField(default="-", max_length=30)),
                (
                    "entry",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("prise", models.PositiveSmallIntegerField()),
                ("unit", models.CharField(blank=True, max_length=100)),
                ("ref_male", models.TextField(blank=True, max_length=5000)),
                ("ref_female", models.TextField(blank=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("result", models.CharField(blank=True, max_length=20)),
                ("ref", models.TextField(blank=True, max_length=5000)),
                ("wrote", models.BooleanField(default=False)),
                ("printed", models.BooleanField(default=False)),
                ("drived", models.BooleanField(default=False)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="homs.patient"
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="homs.test"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="patient",
            name="test",
            field=models.ManyToManyField(through="homs.Result", to="homs.test"),
        ),
    ]