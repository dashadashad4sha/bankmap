from django.db import models


class Workload(models.Model):
    workload_name = models.CharField(max_length=255, verbose_name="Название статуса загруженности")

    def __str__(self):
        return self.workload_name


class Types(models.Model):
    type_name = models.CharField(max_length=255, verbose_name="Тип точки")

    def __str__(self):
        return self.type_name


class Bank(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название отделения банка")
    address = models.CharField(max_length=255, verbose_name="Адрес строкой")
    latitude = models.FloatField(verbose_name="Координата широты")
    longitude = models.FloatField(verbose_name="Координата долготы")
    photo = models.ImageField(upload_to='bank_img', null=True, blank=True, verbose_name='Изображение')
    start_time = models.TimeField(default='00:00', verbose_name='Время открытия')
    end_time = models.TimeField(default='00:00', verbose_name='Время закрытия')

    withdraw_rubles = models.BooleanField(default=False, verbose_name="Возможность снять наличные рубли")
    put_rubles = models.BooleanField(default=False, verbose_name="Возможность положить наличные рубли")
    nfc = models.BooleanField(default=False, verbose_name="Возможность оплаты по NFC")
    withdraw_qr = models.BooleanField(default=False, verbose_name="Возможность снять наличные по QR коду")
    qr_payment = models.BooleanField(default=False, verbose_name="Возможность совершать операции по QR коду")
    for_visually_impaired = models.BooleanField(default=False, verbose_name="Оборудован для слабовидящих")
    for_lm = models.BooleanField(default=False, verbose_name="Оборудован для маломобильных граждан")

    workload = models.ForeignKey('Workload', on_delete=models.PROTECT, null=True, verbose_name="Статус загруженности")
    type = models.ForeignKey('Types', on_delete=models.PROTECT, null=True, verbose_name="Тип точки")

    def __str__(self):
        return self.title
