from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User



class SignUpSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(read_only=True)
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8,write_only=True)
    first_name= serializers.CharField()
    last_name= serializers.CharField()

    class Meta:
        model= User
        fields=["id","email","username","password","first_name","last_name"]

    def Validate(self,attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has been already used")
        return super().validate(attrs)
    
    def create(self,validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    

    
        