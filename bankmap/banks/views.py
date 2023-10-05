from rest_framework import generics
from django.shortcuts import render

from banks.models import Bank, Workload
from banks.serializers import BankSerializer, WorkloadSerializer


class BankAPIView(generics.ListAPIView):
    """Вывод списка всех отделений"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankData(generics.RetrieveAPIView):
    """Вывод информации об отделении по индексу"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class WorkloadAPIView(generics.ListAPIView):
    """Вывод списка загруженностей"""
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer