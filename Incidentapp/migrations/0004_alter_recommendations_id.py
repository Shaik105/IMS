# Generated by Django 5.1.5 on 2025-06-11 03:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidentapp', '0003_alter_followupactions_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendations',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Recommendations', to='Incidentapp.incident_ticket'),
        ),
    ]
