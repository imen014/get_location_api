from rest_framework.serializers import ModelSerializer
from get_location_to_discovert.models import Location

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields= ['city','state','house_number','code_postal']