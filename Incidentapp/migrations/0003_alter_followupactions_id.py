# Generated by Django 5.1.5 on 2025-06-11 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidentapp', '0002_alter_followupactions_id_alter_recommendations_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followupactions',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Follow', to='Incidentapp.incident_ticket'),
        ),
    ]
