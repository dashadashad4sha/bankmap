from rest_framework import serializers

from banks.models import Bank, Workload


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class WorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workload
        fields = "__all__"
