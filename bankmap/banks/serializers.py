from rest_framework import serializers

from banks.models import Bank, Workload, Types


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"
        extra_kwargs = {"start_time": {"format": "%H:%M"},
                        "end_time": {"format": "%H:%M"}}


class WorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workload
        fields = "__all__"


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = "__all__"

