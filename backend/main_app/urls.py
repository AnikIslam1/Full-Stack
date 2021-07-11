
from django.db import router
from django.urls import path
from rest_framework import routers #router import
from .views import RegistersViewSet


#router config
router = routers.DefaultRouter()
router.register('register', RegistersViewSet)

urlpatterns = router.urls
