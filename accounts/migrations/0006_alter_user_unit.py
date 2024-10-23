# Generated by Django 5.1.2 on 2024-10-23 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unit',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='unit_account', to='accounts.unit'),
        ),
    ]
