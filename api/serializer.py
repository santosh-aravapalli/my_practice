from hospital_admin.models import *
from rest_framework.viewsets import ModelViewSet


class physicianserializer(ModelViewSet):

    class Meta:
        model = physician
        fields = "__all__"


