from rest_framework import serializers

from charitable.models import User, NonGo, Administrator, Don


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_administrator']

class AdministratorSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password2']
        extra_kwags={
            'password':{'write_only':True}
        }
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error": "Your passwords do not match!"})
            
        user.set_password(password)
        user.is_administrator=True
        user.save()
        Administrator.objects.create(user=user)
        return user



class NonGoSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email', 'password', 'password2']
        extra_kwags={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error": "Your passwords do not match!"})
            
        user.set_password(password)
        user.is_NonGo=True
        user.save()
        NonGo.objects.create(user=user)
        return user

class DonSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password2']
        extra_kwags={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error": "Your passwords do not match!"})
            
        user.set_password(password)
        user.is_Don=True
        user.save()
        Don.objects.create(user=user)
        return user