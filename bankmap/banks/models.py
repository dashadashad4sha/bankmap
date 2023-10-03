from django.db import models


class Workload(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название статуса загруженности")

    def __str__(self):
        return self.title


class Bank(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название отделения банка")
    address = models.CharField(max_length=255, verbose_name="Адрес строкой")
    latitude = models.FloatField(verbose_name="Координата широты")
    longitude = models.FloatField(verbose_name="Координата долготы")
    photo = models.ImageField(upload_to='bank_img', null=True, blank=True, verbose_name='Изображение')

    can_withdraw_cash = models.BooleanField(default=False, verbose_name="Возможность снять наличные")
    employees = models.BooleanField(default=False, verbose_name="На отделении есть сотрудники")
    can_deposit_money = models.BooleanField(default=False, verbose_name="Возможность положить наличные")

    workload = models.ForeignKey('Workload', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
