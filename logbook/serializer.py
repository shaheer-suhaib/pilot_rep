from rest_framework.serializers import ModelSerializer
from .models import FlightLog

class FlighLOgSerializer(ModelSerializer):   # This helps convert model ↔ JSON automatically.
    class Meta:
        model = FlightLog
        fields = '__all__'