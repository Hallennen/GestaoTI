# Generated by Django 5.1.2 on 2024-12-03 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_acontuser_path'),
        ('aplication', '0012_ferias'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ferias',
            name='month',
            field=models.CharField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='end_vacation',
            field=models.DateField(verbose_name='Data Fim'),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='pessoa_vacation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ferias_pessoa', to=settings.AUTH_USER_MODEL, verbose_name='Colaborador'),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='start_vacation',
            field=models.DateField(unique=True, verbose_name='Data inicio:'),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ferias_unidade', to='accounts.unit', verbose_name='Unidade'),
        ),
    ]
