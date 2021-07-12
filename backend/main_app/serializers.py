# from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import RegisterModel

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = RegisterModel
        fields = [
            'id',
            'name',
            'mail',
            'password',
        ]
    
    def validate(self, attrs):
        if RegisterModel.objects.filter(mail = attrs['mail']).exists():
            raise serializers.ValidationError(
                {'Email is already in use'}
            )
        return super().validate(attrs)

#         extra_kwords = {
#             # not needed now
#         }

