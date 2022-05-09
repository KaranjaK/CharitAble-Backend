from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import NGOSerializer, DonorSerializer, RequestsSerializer, AdminSerializer
from charitable.models import NGO, Donor, Admin, Requests
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import Http404
from django.contrib import messages




#api views
class NGOList(APIView):
    def get(self, request, format=None):
        all_ngos = NGO.objects.all()
        serializers = NGOSerializer(all_ngos, many=True)
        return Response(serializers.data)
        

    def post(self, request, format=None):
        serializers = NGOSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class NGODescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_ngo(self, pk):
        try:
            return NGO.objects.get(pk=pk)
        except NGO.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        ngo = self.get_ngo(pk)
        serializers = NGOSerializer(ngo)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        ngo = self.get_ngo(pk)
        serializers = NGOSerializer(ngo, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ngo = self.get_ngo(pk)
        ngo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonorList(APIView):
    def get(self, request, format=None):
        all_donors = Donor.objects.all()
        serializers = DonorSerializer(all_donors, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = DonorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class DonorDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_donor(self, pk):
        try:
            return Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        donor = self.get_donor(pk)
        serializers = DonorSerializer(donor)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        donor = self.get_donor(pk)
        serializers = DonorSerializer(donor, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        donor = self.get_donor(pk)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RequestsList(APIView):
    def get(self, request, format=None):
        all_requests = Requests.objects.all()
        serializers = RequestsSerializer(all_requests, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = RequestsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

    

class RequestsDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_request(self, pk):
        try:
            return Requests.objects.get(pk=pk)
        except Requests.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        request = self.get_request(pk)
        serializers = RequestsSerializer(request)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        request = self.get_request(pk)
        serializers = RequestsSerializer(request, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        request = self.get_request(pk)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminList(APIView):
    def get(self, request, format=None):
        all_admins = Admin.objects.all()
        serializers = AdminSerializer(all_admins, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AdminSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class AdminDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_admin(self, pk):
        try:
            return Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        admin = self.get_admin(pk)
        serializers = AdminSerializer(admin)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        admin = self.get_admin(pk)
        serializers = AdminSerializer(admin, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        admin = self.get_admin(pk)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 