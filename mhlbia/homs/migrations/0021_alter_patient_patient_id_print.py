# Generated by Django 5.0.3 on 2024-03-25 17:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homs', '0020_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(default='936163461659', editable=False, max_length=12, unique=True),
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('print_count', models.IntegerField(default=0)),
                ('result', models.ManyToManyField(to='homs.result')),
            ],
        ),
    ]
