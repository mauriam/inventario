from rest_framework import serializers
from .models import *

class TpsNationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=TpsNationalityModel
        fields='__all__'
        extra_kwargs={
            'nationality_id':{
                'read_only':True,
            }
        }

class TpsStateSerializer(serializers.ModelSerializer):
    class Meta:
        model=TpsStateModel
        fields='__all__'

class TpsMunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=TpsMunicipalityModel
        fields='__all__'

class TpsCitySerializer(serializers.ModelSerializer):
    class Meta:
        model=TpsCityModel
        fields='__all__'

class TpsParishCouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model=TpsParishCouncilModel
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddressModel
        fields='__all__'