from rest_framework import serializers
from .models import NGO, Donor, Requests, Admin

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = ('id', 'name', 'logo','category', 'description', 'web_link', 'contact', 'email', 'location')

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ('id', 'name', 'type', 'web_link', 'contact', 'email', 'location')

class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'fin_statements', 'reports', 'amount_range', 'verification')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'username')
        