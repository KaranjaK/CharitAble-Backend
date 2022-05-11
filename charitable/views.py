from django.shortcuts import render, redirect
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import NonGoSerializer, DonSerializer, RequestsSerializer, AdministratorSerializer
from charitable.models import Administrator, NonGo, Don, Administrator, NonGo, Requests
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import Http404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

# def signup(request):
#     if request.method == "POST":
#          username = request.POST["username"]
#          password = request.POST["password"]
#          email = request.POST["email"]
#          user = User.objects.create_user(
#                 username = username,
#                 password = password,
#                 email =email)

#          subject = 'welcome to CharitAble'
#          message = f'Hello {user.username}, thank you for registering in CharitAble, where kindness is the language!'
#          email_from = settings.EMAIL_HOST_USER
#          recipient_list = [user.email,]
#          send_mail( subject, message, email_from, recipient_list )
#          return redirect ("/homepage/")

# subject = 'welcome to CharitAble'
# message = f' Thank you for chhoosing CharitAble, where kindness is the language!'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = []
# send_mail( subject, message, email_from, recipient_list )


#api views
class NonGoList(APIView):
    def get(self, request, format=None):
        all_ngos = NonGo.objects.all()
        serializers = NonGoSerializer(all_ngos, many=True)
        return Response(serializers.data)
        

    def post(self, request, format=None):
        serializers = NonGoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class NonGoDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_ngo(self, pk):
        try:
            return NonGo.objects.get(pk=pk)
        except NonGo.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        ngo = self.get_ngo(pk)
        serializers = NonGoSerializer(ngo)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        ngo = self.get_ngo(pk)
        serializers = NonGoSerializer(ngo, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ngo = self.get_ngo(pk)
        ngo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonList(APIView):
    def get(self, request, format=None):
        all_donors = Don.objects.all()
        serializers = DonSerializer(all_donors, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = DonSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class DonDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_donor(self, pk):
        try:
            return Don.objects.get(pk=pk)
        except Don.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        donor = self.get_donor(pk)
        serializers = DonSerializer(donor)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        donor = self.get_donor(pk)
        serializers = DonSerializer(donor, request.data)
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

class AdministratorList(APIView):
    def get(self, request, format=None):
        all_admins = Administrator.objects.all()
        serializers = AdministratorSerializer(all_admins, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AdministratorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class AdministratorDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_admin(self, pk):
        try:
            return Administrator.objects.get(pk=pk)
        except Administrator.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        admin = self.get_admin(pk)
        serializers = AdministratorSerializer(admin)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        admin = self.get_admin(pk)
        serializers = AdministratorSerializer(admin, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        admin = self.get_admin(pk)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


