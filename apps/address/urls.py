from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'nationality',TpsNationalityApiViewSet)
router.register(r'state',TpsStateApiViewSet)
router.register(r'municipality',TpsMunicipalityApiViewSet)
router.register(r'city',TpsCityApiViewSet)
router.register(r'parishcountil',TpsParishCouncilApiViewSet)
router.register(r'addres',AddressApiViewSet)

urlpatterns = router.urls