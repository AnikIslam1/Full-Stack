# from django.db import models
# from django.db.models import fields
# from rest_framework import serializers
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
#         extra_kwords = {
#             # not needed now
#         }