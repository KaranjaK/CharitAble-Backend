from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import AdminSignupSerializer, DonorSignupSerializer, NgoSignupSerializer, UserSerializer


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