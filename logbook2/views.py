from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Pilot, Checker, Aircraft, FlightCategory, FlightLog
from .serializer import UserSerializer, AircraftSerializer, FlightCategorySerializer, FlightLogSerializer, PilotSerializer, CheckerSerializer

# Create a new user
@api_view(['POST'])
def create_user(request):
        
    data = request.data     # get 
    user = User.objects.create(
            email=data['email'],
            id=data['id'],
            name=data['name'],
            is_active=data['is_active'],
            is_staff=data['is_staff']
        )
    serialzed = UserSerializer(user,many=False)
    
    return Response(serialzed.data)  # ends the serialized data back to the client as a response 

   

@api_view(['POST'])
def create_pilot(request):
    try:
        # Extract user data
        email = request.data['email']
        user_id = request.data['id']
        name = request.data['name']
        
        # Create the User object
        user = User.objects.create_user(email=email, id=user_id,name=name)
        
        # Create the Pilot object, linked to the user
        pilot = Pilot.objects.create(pilot_id=user)
        
        # Send response
        serializer = PilotSerializer(pilot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except KeyError as e:
        return Response({"detail": f"Missing key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_checker(request):
    try:
        # Extract user data
        email = request.data['email']
     
        user_id = request.data['id']
        name = request.data['name']
        
        # Create the User object
        user = User.objects.create_user(email=email, id=user_id, name= name)
        
        # Create the Checker object, linked to the user
        checker = Checker.objects.create(user_id=user)
        
        # Send response
        serializer = CheckerSerializer(checker)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except KeyError as e:
        return Response({"detail": f"Missing key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Insert aircraft for the user
@api_view(['POST'])
def post_aircraft_for_user(request, user_id):
     
     data = request.data     # get 
     try:
            user = User.objects.get(id=user_id)
     except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
     
     obj = Aircraft.objects.create(type =data['type'])
     
     serialzed = AircraftSerializer(obj,many=False)
    
     return Response(serialzed.data)  # ends the serialized data back to the client as a response 



# Insert flight category for the user
@api_view(['POST'])
def postF_category_for_user(request, user_id):
     data = request.data     # get 
     try:
            user = User.objects.get(id=user_id)
     except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
     
     obj = FlightCategory.objects.create(engine = data['engine'],role = data['role'])
     
     serialzed = FlightCategorySerializer(obj,many=False)
    
     return Response(serialzed.data)  # ends the serialized data back to the client as a response 

@api_view(['POST'])
def post_flight_log_for_user(request, user_id, AirCraID, FlighCatID):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)   #change to
            aircrft = Aircraft.objects.get(aircraft_id=AirCraID)
            F_cat = FlightCategory.objects.get(category_id=FlighCatID)

        except (User.DoesNotExist, Aircraft.DoesNotExist, FlightCategory.DoesNotExist):
            return Response({"detail": "User, Aircraft, or Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        
        obj = FlightLog.objects.create(
            date=data['date'],
            route=data['route'],
            remarks=data['remarks'],
            duration=data['duration'],
            pilot_id=Pilot.objects.get(pilot_id=user_id),       
            aircraft_id= aircrft,                           
            category_id= F_cat


            )

        serializer = FlightLogSerializer(obj, many=False)

        return Response(serializer.data)
