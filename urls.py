#from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import EmpViewSet3
router=DefaultRouter()
router.register('emp-viewset',EmpViewSet3,base_name='emp-viewset')
urlpatterns = [
    url(r"", include(router.urls)),
]