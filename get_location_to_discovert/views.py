from django.shortcuts import render
from get_location_to_discovert.serializers import LocationSerializer
from rest_framework.viewsets import ModelViewSet
from get_location_to_discovert.models import Location

class LocationView(ModelViewSet):
    
    serializer_class = LocationSerializer
    def get_queryset(self,*args,**kwargs):
        locations = Location.objects.all()
        return locations
