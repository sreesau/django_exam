from medisite.models import MedicineDetails
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MedicineDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDetails
        fields = ('name', 'quantity', 'price', 'mfg_date','exp_date')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField( required=True,validators=[UniqueValidator(queryset=User.objects.all())]      )
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")

        return data
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password1']
        )
        user.save()
        return user
