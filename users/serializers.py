from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class SimpleCustomUserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for register simple user.
    """

    username = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=models.CustomSimpleUser.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=models.CustomSimpleUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.CustomSimpleUser
        fields = ['username', 'email', 'phone_number', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.pop('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match"})

        attrs['password'] = password
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.CustomSimpleUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
