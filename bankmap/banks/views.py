from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from django.shortcuts import render
from rest_framework import filters
from rest_framework.views import APIView

from banks.models import Bank, Workload, Types
from banks.serializers import BankSerializer, WorkloadSerializer, TypesSerializer
from rest_framework.response import Response


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

    def get_object(self):
        obj = super().get_object()
        print("gooo")
        obj.counter()
        return obj


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
    """Фильтрация.

    В GET передаются True/False у полей

    for_lm,
    withdraw_rubles,
    withdraw_rubles,
    nfc,
    qr_payment,
    withdraw_qr,
    for_visually_impaired,
    for_lm,

    Отдельно можно передать значение для атрибута type и workload

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

        type = self.request.query_params.get('type')
        workload = self.request.query_params.get('workload')

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

        if not type is None:
            queryset = queryset.filter(type=type)

        if not workload is None:
            queryset = queryset.filter(workload=workload)

        return queryset


class SearchView(generics.ListAPIView):
    """Поиск (по полям Заголовок и Адрес)

    В get передается search=строка поиска

    """

    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$title', '$address']


class BankAPICoords(generics.ListAPIView):
    """Ближайшие отделения

    параметры latitude longitude
    """
    serializer_class = BankSerializer

    def get_queryset(self):
        queryset = Bank.objects.all()

        def coord_filter(queryset):
            latitude = float(self.request.query_params.get('latitude'))
            longitude = float(self.request.query_params.get('longitude'))

            queryset = queryset.filter(latitude__gte=latitude - 0.1, latitude__lte=latitude + 0.1)
            queryset = queryset.filter(longitude__gte=longitude - 0.1, longitude__lte=longitude + 0.1)
            return queryset

        return coord_filter(queryset)


class FilteredListViewCoord(generics.ListAPIView):
    """Фильтрация с координатами.

    параметры latitude longitude обязательны

    В GET передаются True/False у полей

    for_lm,
    withdraw_rubles,
    withdraw_rubles,
    nfc,
    qr_payment,
    withdraw_qr,
    for_visually_impaired,
    for_lm,

    Отдельно можно передать значение для атрибута type и workload

    Пример: http://127.0.0.1:8000/api/filteredbanklist?for_visually_impaired=True&put_rubles=False&withdraw_qr=True
    """
    serializer_class = BankSerializer

    def get_queryset(self):
        """
        Возвращает отделения на основе переданных
        в get запросе данных
        """
        queryset = Bank.objects.all()

        def coord_filter(queryset):
            latitude = float(self.request.query_params.get('latitude'))
            longitude = float(self.request.query_params.get('longitude'))

            queryset = queryset.filter(latitude__gte=latitude - 0.1, latitude__lte=latitude + 0.1)
            queryset = queryset.filter(longitude__gte=longitude - 0.1, longitude__lte=longitude + 0.1)
            return queryset

        queryset = coord_filter(queryset)

        withdraw_rubles = self.request.query_params.get('withdraw_rubles')
        put_rubles = self.request.query_params.get('put_rubles')
        nfc = self.request.query_params.get('nfc')
        withdraw_qr = self.request.query_params.get('withdraw_qr')
        qr_payment = self.request.query_params.get('qr_payment')
        for_visually_impaired = self.request.query_params.get('for_visually_impaired')
        for_lm = self.request.query_params.get('for_lm')

        type = self.request.query_params.get('type')
        workload = self.request.query_params.get('workload')

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

        if not type is None:
            queryset = queryset.filter(type=type)

        if not workload is None:
            queryset = queryset.filter(workload=workload)

        return queryset


class ButtonGetRoutCount(APIView):
    """Подсчёт количества построений маршрута

       Передается id

       Пример запроса:

       http://127.0.0.1:8000/api/button_get_pressed/?id=17
    """

    def post(self, request):
        id = request.query_params.get('id')
        button = Bank.objects.get(id=id)
        button.total_get_rout += 1
        button.save()
        serializer = BankSerializer(button)
        return Response(serializer.data)


class UpdateWorkload(APIView):
    """Обновление загруженности отделений

       Выполняется каждые полчаса, чтобы на основе данных за
       прошедшие почаса обновить данные о загруженности отделений.
    """

    def update_workload(self):
        for obj in Bank.objects.all():
            if obj.total_views >= 20 and obj.total_get_rout >= 5:
                obj.workload_id = 1
            elif obj.total_views >= 10:
                obj.workload_id = 2
            else:
                obj.workload_id = 3
            obj.total_views = 0
            obj.total_get_rout = 0
            obj.save()

    def post(self, request):
        self.update_workload()
        serializer = BankSerializer()
        return Response(serializer.data)
