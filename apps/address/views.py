from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class TpsNationalityApiViewSet(ModelViewSet):
    serializer_class=TpsNationalitySerializer
    queryset=TpsNationalityModel.objects.all()

class TpsStateApiViewSet(ModelViewSet):
    serializer_class=TpsStateSerializer
    queryset=TpsStateModel.objects.all()

class TpsMunicipalityApiViewSet(ModelViewSet):
    serializer_class=TpsMunicipalitySerializer
    queryset=TpsMunicipalityModel.objects.all()


class TpsCityApiViewSet(ModelViewSet):
    serializer_class=TpsCitySerializer
    queryset=TpsCityModel.objects.all()


class TpsParishCouncilApiViewSet(ModelViewSet):
    serializer_class=TpsParishCouncilSerializer
    queryset=TpsParishCouncilModel.objects.all()

class AddressApiViewSet(ModelViewSet):
    serializer_class=AddressSerializer
    queryset=AddressModel.objects.all()