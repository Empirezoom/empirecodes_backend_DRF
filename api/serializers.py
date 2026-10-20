from rest_framework import serializers
from .models import ClientLead, ClientReview, SystemMetric, ContractBooking, ContractMessage

class ClientLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLead
        fields = '__all__'


class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = '__all__'


class SystemMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMetric
        fields = '__all__'


class ContractMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractMessage
        fields = '__all__'


class ContractBookingSerializer(serializers.ModelSerializer):
    messages = ContractMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ContractBooking
        fields = '__all__'


