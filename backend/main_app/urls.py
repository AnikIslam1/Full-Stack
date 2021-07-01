
from django.db import router
from django.urls import path
from rest_framework import routers
from .views import RegistersViewSet



router = routers.DefaultRouter()
router.register('register', RegistersViewSet)

urlpatterns = router.urls
