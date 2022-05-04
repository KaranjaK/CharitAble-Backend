from rest_framework import serializers

from charitable.models import User, Ngo, Admin, Donor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_admin']

class AdminSignupSerializer(serializers.ModelSerializer):
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
        user.is_admin=True
        user.save()
        Admin.objects.create(user=user)
        return user



class NgoSignupSerializer(serializers.ModelSerializer):
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
        user.is_Ngo=True
        user.save()
        Ngo.objects.create(user=user)
        return user

class DonorSignupSerializer(serializers.ModelSerializer):
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
        user.is_Donor=True
        user.save()
        Donor.objects.create(user=user)
        return user