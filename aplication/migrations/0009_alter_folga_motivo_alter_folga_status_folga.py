# Generated by Django 5.1.2 on 2024-11-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0008_alter_folga_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folga',
            name='motivo',
            field=models.CharField(choices=[('DOMINGO TRABALHADO', 'TRABALHADO'), ('COMBINADO GESTOR', 'COMBINADO'), ('OUTROS', 'OUTROS')], max_length=25),
        ),
        migrations.AlterField(
            model_name='folga',
            name='status_folga',
            field=models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('APROVADO', 'APROVADO'), ('RECUSADO', 'RECUSADO')], default='PENDENTE', max_length=25),
        ),
    ]
