from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Pilot, Checker, Aircraft, FlightCategory, FlightLog
from .serializer import UserSerializer, AircraftSerializer, FlightCategorySerializer, FlightLogSerializer, PilotSerializer, CheckerSerializer
from datetime import datetime
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
        email = request.data.get('email')
        user_id = request.data('id')
        name = request.data('name')
        
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
     
     obj = Aircraft.objects.create(type =data['type'], tail_no=data['tail_no'])
     
     serialzed = AircraftSerializer(obj,many=False)
    
     return Response(serialzed.data)  # ends the serialized data back to the client as a response 




@api_view(['POST'])
def post_flight_log_for_user(request, user_id):
   
       # print(request.data)
    
       # Step 1: Create Aircraft
        typee = request.data.get('typee')
        tail_no = request.data.get('tail_no')
        aircraft_obj = Aircraft.objects.create(typee=typee, tail_no=tail_no)

        
        # Step 2: Create FlightCategory
        engine = request.data.get('engine')
        role = request.data.get('role')
        mission = request.data.get('mission')
        flight_cat_obj = FlightCategory.objects.create(engine=engine, role=role, mission=mission)
        
      
        # Step 3: Now create FlightLog
        try:
            pilot = Pilot.objects.get(pilot_id=user_id)
        except (User.DoesNotExist, Pilot.DoesNotExist):
            return Response({"detail": "User or Pilot not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        date_str = data.get('date')
        take_off_time_str = data.get('Take_off_time')
        landing_time_str = data.get('Landing_time')

        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
        take_off_time_obj = datetime.fromisoformat(take_off_time_str.replace('Z', '+00:00')) if take_off_time_str else None
        landing_time_obj = datetime.fromisoformat(landing_time_str.replace('Z', '+00:00')) if landing_time_str else None


        obj = FlightLog.objects.create(
            date=date_obj, #data.get('date'),
            route=data.get('route'),
            Additional_note=data.get('Additional_note'),
            duration=data.get('duration'),
            Pilot_in_comm=data.get('Pilot_in_comm'),
            Co_Pilot=data.get('Co_Pilot'),
            Take_off_time=take_off_time_obj,
            Landing_time=landing_time_obj,
            Instrument_Flu=data.get('Instrument_Flu'),
            Day_night=data.get('Day_night'),
            pilot_id=Pilot.objects.get(pilot_id=user_id),
            aircraft_id=aircraft_obj,
            category_id=flight_cat_obj
        )
       # obj.refresh_from_db()  # 🔥 Add this after create


        serializer = FlightLogSerializer(obj, many=False)

        return Response(serializer.data)


@api_view(['PUT'])
def apply_read(request, mission_id):
  try:
        # Fetch the FlightLog object with the specified pilot_id
        obj = FlightLog.objects.filter(id=mission_id)
        obj.update(read=True)

        #save might work........
        
      

        return Response({"message": "Read status updated successfully"}, status=status.HTTP_200_OK)
    
  except FlightLog.DoesNotExist:
        return Response({"error": "FlightLog with this pilot_id not found"}, status=status.HTTP_404_NOT_FOUND)
     
     


@api_view(['GET'])
def get_flight_log(request):
    if request.method == 'GET':
        # Get the 'read' parameter from the query string
        read = request.query_params.get('read', None)

        flight_logs = FlightLog.objects.all()

        # Apply filters based on the presence of parameters
        if read is not None:  # Check if 'read' is provided in the query params
            if read.lower() == 'false':  # If read is 'false', filter for False values
                flight_logs = flight_logs.filter(read=False)
          

      
        serializer = FlightLogSerializer(flight_logs, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def filter_flight_logs(request):
    # Extract filter parameters from the request
    pilot_id = request.query_params.get('pilot_id', None)
    route = request.query_params.get('route', None)
    all_pilot = request.query_params.get('All_pilot', None)
    all_route = request.query_params.get('All_route', None)

    # Start with all flight logs
    flight_logs = FlightLog.objects.all()

    # Apply filters based on the query parameters
    if pilot_id:
        flight_logs = flight_logs.filter(pilot_id=pilot_id)

    if route:
        flight_logs = flight_logs.filter(route=route)

    if all_pilot == 'true':
        flight_logs = flight_logs.all()  # No filter on pilot, get all pilots

    if all_route == 'true':
        flight_logs = flight_logs.all()  # No filter on route, get all routes

    # Serialize the filtered queryset
    serializer = FlightLogSerializer(flight_logs, many=True)

    # Return the response
    return Response(serializer.data)



@api_view(['GET'])
def get_marked(request):
     
    Marked_logs = FlightLog.objects.filter(read=True)

    serializer = FlightLogSerializer(Marked_logs, many=True)

  
    return Response(serializer.data)

