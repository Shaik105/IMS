# Generated by Django 5.1.5 on 2025-06-11 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followupactions',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Up', to='Incidentapp.incident_ticket'),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re', to='Incidentapp.incident_ticket'),
        ),
    ]
