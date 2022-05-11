from rest_framework import serializers
from .models import NonGo, Don, Requests, Administrator

class NonGoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonGo
        fields = ('id', 'user', 'company_name','email', 'password')

class DonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Don
        fields = ('id', 'user', 'Don_name',  'contact', 'email', 'password')

class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'fin_statements', 'reports', 'amount_range', 'verification')

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id', 'user', 'email', 'password')
        