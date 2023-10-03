# Generated by Django 4.2.5 on 2023-10-03 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название статуса загруженности')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название отделения банка')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес строкой')),
                ('latitude', models.FloatField(verbose_name='Координата широты')),
                ('longitude', models.FloatField(verbose_name='Координата долготы')),
                ('can_withdraw_cash', models.BooleanField(default=False, verbose_name='Возможность снять наличные')),
                ('employees', models.BooleanField(default=False, verbose_name='На отделении есть сотрудники')),
                ('can_deposit_money', models.BooleanField(default=False, verbose_name='Возможность положить наличные')),
                ('workload', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='banks.workload')),
            ],
        ),
    ]
