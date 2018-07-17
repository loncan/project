from .models import Emp
from .serializers import EmpSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
class EmpViewSet3(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (BasicAuthentication,)
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
