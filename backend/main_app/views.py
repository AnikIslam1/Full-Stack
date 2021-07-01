# from django.db.models.base import Model
# from django.shortcuts import render
# from typing import Generic
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.views.generic import GenericViewError, TemplateView
# from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import RegisterModel
from .serializers import RegisterSerializer

#Page Test
# def homeView(request):
#     return HttpResponse("Hello")

class RegistersViewSet(ModelViewSet):
    queryset = RegisterModel.objects.all()
    serializer_class = RegisterSerializer

#index.html link
# class HomeView(TemplateView):
#     template_name = "index.html"


#Rest API part Admin
# class RegisterView(generics.CreateAPIView):
#     queryset = Register.objects.all()
#     serializer_class = RegisterSerializer

# class RegisterDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Register.objects.all()
#     serializer_class = RegisterSerializer

#RegisterAPI
#functions
# def index(request):
#     # registers = RegisterModel.objects.all()
#     registers = []
#     for r in RegisterModel.objects.all():
#         registers.append({
#             'name': register.name,
#             'mail': register.mail,
#         }) 

#     return JsonResponse(registers, safe=False)




