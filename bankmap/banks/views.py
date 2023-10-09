from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from django.shortcuts import render

from banks.models import Bank, Workload, Types
from banks.serializers import BankSerializer, WorkloadSerializer, TypesSerializer


class BankAPIView(generics.ListAPIView):
    """Список всех точек

    Вывод списка всех отделений"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankData(generics.RetrieveAPIView):
    """Один банк по индексу

    Вывод информации об отделении по индексу"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class WorkloadAPIView(generics.ListAPIView):
    """Виды загруженности

    Вывод списка загруженностей"""
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer


class TypesAPIView(generics.ListAPIView):
    """Типы точек

    Вывод списка типов точек"""
    queryset = Types.objects.all()
    serializer_class = TypesSerializer


class FilteredListView(generics.ListAPIView):
    """Фильтрация. Тестирование. Не использовать.

    В GET передаются True/False у полей

    for_lm,
    withdraw_rubles,
    withdraw_rubles,
    nfc,
    qr_payment,
    withdraw_qr,
    for_visually_impaired,
    for_lm,

    Пример: http://127.0.0.1:8000/api/filteredbanklist?for_visually_impaired=True&put_rubles=False&withdraw_qr=True
    """
    serializer_class = BankSerializer

    def get_queryset(self):
        """
        Возвращает отделения на основе переданных
        в get запросе данных
        """
        queryset = Bank.objects.all()

        withdraw_rubles = self.request.query_params.get('withdraw_rubles')
        put_rubles = self.request.query_params.get('put_rubles')
        nfc = self.request.query_params.get('nfc')
        withdraw_qr = self.request.query_params.get('withdraw_qr')
        qr_payment = self.request.query_params.get('qr_payment')
        for_visually_impaired = self.request.query_params.get('for_visually_impaired')
        for_lm = self.request.query_params.get('for_lm')

        parameters_list = {"withdraw_rubles": withdraw_rubles,
                           "put_rubles": put_rubles,
                           "nfc": nfc,
                           "withdraw_qr": withdraw_qr,
                           "qr_payment": qr_payment,
                           "for_visually_impaired": for_visually_impaired,
                           "for_lm": for_lm}

        for k in parameters_list:

            if parameters_list[k]:

                if k == "withdraw_rubles":
                    queryset = queryset.filter(withdraw_rubles=True)

                elif k == "put_rubles":
                    queryset = queryset.filter(put_rubles=True)

                elif k == "nfc":
                    queryset = queryset.filter(nfc=True)

                elif k == "withdraw_qr":
                    queryset = queryset.filter(withdraw_qr=True)

                elif k == "qr_payment":
                    queryset = queryset.filter(qr_payment=True)

                elif k == "for_visually_impaired":
                    queryset = queryset.filter(for_visually_impaired=True)

                elif k == "for_lm":
                    queryset = queryset.filter(for_lm=True)

        return queryset
