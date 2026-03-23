from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email',  'password']

    def validate_username(self, value):
        value = value.strip().lower()

        if ' ' in value:
            raise serializers.ValidationError(
                'Username não pode conter espaços.'
            )

        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('Username já existe.')

        return value

    def create(self, validated_data):
        validated_data['username'] = validated_data['username'].lower()
        user = User.objects.create_user(**validated_data)

        return user


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']
