from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AdministratorSignupSerializer, DonSignupSerializer, NonGoSignupSerializer, UserSerializer
from .permissions import IsAdministratorUser, IsNonGoUser, IsDonUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import  redirect

# creating my views

class AdministratorSignupView(generics.GenericAPIView):
    serializer_class= AdministratorSignupSerializer
    def post (self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "You have succesfully created your account!"
        })

class NonGoSignupView(generics.GenericAPIView):
    serializer_class= NonGoSignupSerializer
    def post (self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "You have succesfully created your account!"
        })
    
    def signup(request):
         if request.method == "POST":
              company_name = request.POST["Don_name"]
              password = request.POST["password"]
              email = request.POST["email"]
              user = User.objects.create_user(
                     Don_name = company_name,
                     password = password,
                     email =email)
        

              subject = 'welcome to CharitAble'
              message = f'Hello {user.company_name}, thank you for registering in CharitAble, where kindness is the language!'
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [user.email,]
              send_mail( subject, message, email_from, recipient_list )
              return redirect ("/homepage/")


class DonSignupView(generics.GenericAPIView):
    serializer_class= DonSignupSerializer
    def post (self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "You have succesfully created your account!"
        })
    def signup(request):
         if request.method == "POST":
              Don_name = request.POST["Don_name"]
              password = request.POST["password"]
              email = request.POST["email"]
              user = User.objects.create_user(
                     Don_name = Don_name,
                     password = password,
                     email =email)
        

              subject = 'welcome to CharitAble'
              message = f'Hello {user.Don_name}, thank you for registering in CharitAble, where kindness is the language!'
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [user.email,]
              send_mail( subject, message, email_from, recipient_list )
              return redirect ("/homepage/")
   

class CustomeAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id': user.pk,
            'is_Ngo':user.is_NonGo
        })

class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class AdministratorOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsAdministratorUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class NonGoOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsNonGoUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user
    
class DonOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsDonUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['Don_name'] = user.Don_name
        

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        'signup/admin/',
        'signup/ngo/',
        'signup/donor/',
        'login/',
        'logout/',
        'Admin/dashboard/',
        'Ngo/dashboard/',
        'Donor/dashboard/'

    ]

    return Response(routes)

