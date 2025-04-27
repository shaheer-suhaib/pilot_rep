from rest_framework import serializers
from .models import User, Pilot, Checker, Aircraft, FlightCategory, FlightLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'is_active', 'is_staff']

class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ['pilot_id']

class CheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checker
        fields = ['user_id']

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = [ 'typee','tail_no']

class FlightCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightCategory
        fields = [ 'engine', 'role','mission']

class FlightLogSerializer(serializers.ModelSerializer):
    pilot_id = PilotSerializer()
    aircraft_id = AircraftSerializer()
    category_id = FlightCategorySerializer()

    class Meta:
        model = FlightLog
        fields = [ 'date', 'route', 'Additional_note', 'duration', 'Pilot_in_comm','Co_Pilot','Take_off_time','Landing_time','Instrument_Flu','Day_night','pilot_id', 'aircraft_id', 'category_id','read']
