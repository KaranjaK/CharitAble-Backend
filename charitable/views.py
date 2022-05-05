
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
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         email = request.POST["email"]
         user = User.objects.create_user(
                username = username,
                password = password,
                email =email)

         subject = 'welcome to CharitAble'
         message = f'Hello dear, thank you for registering in CharitAble, where kindness is the language!'
         email_from = settings.EMAIL_HOST_USER
         recipient_list = []
         send_mail( subject, message, email_from, recipient_list )
         return redirect ("/homepage/")




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

from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login



# Create your views here.

def index(request):
    return render (request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'succesfully created user'
            return redirect('login_view')
        else:
            msg= 'form is not valid'
    else:
        form=SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_Ngo:
                login(request, user)
                return redirect('Ngo')
            elif user is not None and user.is_Donor:
                login(request, user)
                return redirect('donor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def Ngo(request):
    return render(request,'ngo.html')


def Donor(request):
    return render(request,'Donor.html')