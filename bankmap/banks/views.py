from rest_framework import generics
from django.shortcuts import render

from banks.models import Bank, Workload
from banks.serializers import BankSerializer, WorkloadSerializer


class BankAPIView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankData(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class WorkloadAPIView(generics.ListAPIView):
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer