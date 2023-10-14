# Generated by Django 4.2.5 on 2023-10-14 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0004_alter_bank_workload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='workload',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.PROTECT, to='banks.workload', verbose_name='Статус загруженности'),
        ),
    ]