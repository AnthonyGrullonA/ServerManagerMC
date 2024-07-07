# Generated by Django 5.0.6 on 2024-07-07 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='enterprise',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='enterprise.enterprise'),
            preserve_default=False,
        ),
    ]
