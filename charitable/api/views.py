from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AdminSignupSerializer, DonorSignupSerializer, NgoSignupSerializer, UserSerializer
from .permissions import IsAdminUser, IsNgoUser, IsDonorUser


class AdminSignupView(generics.GenericAPIView):
    serializer_class= AdminSignupSerializer
    def post (self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "You have succesfully creates your account!"
        })

class NgoSignupView(generics.GenericAPIView):
    serializer_class= NgoSignupSerializer
    def post (self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "You have succesfully creates your account!"
        })


class DonorSignupView(generics.GenericAPIView):
    serializer_class= DonorSignupSerializer
    def post (self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "You have succesfully creates your account!"
        })

class CustomeAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id': user.pk,
            'is_Ngo':user.is_Ngo
        })

class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class AdminOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsAdminUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class NgoOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsNgoUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user
    
class DonorOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsDonorUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user