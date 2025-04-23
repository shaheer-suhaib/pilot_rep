from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import FlighLOgSerializer
from .models import FlightLog


@api_view(['GET'])
def getLog(request):
    data = FlightLog.objects.all()
    serialzed = FlighLOgSerializer(data,many=True)
    
    return Response(serialzed.data)
    


@api_view(['GET'])  #takes in the request sent by the client 
def getAirCraft(request,A_type):

    data = FlightLog.objects.filter(aircraft_type = A_type)
    serialzed = FlighLOgSerializer(data,many=True)
    
    return Response(serialzed.data)


@api_view(['POST'])
def create(request):

    data = request.data     # get 
    obj = FlightLog.objects.create(
        aircraft_type = data['aircraft_type']      #  extract this

    )

    serialzed = FlighLOgSerializer(obj,many=False)
    
    return Response(serialzed.data)  # ends the serialized data back to the client as a response 

@api_view(['PUT'])
def update(request, pk):
    try:
        obj = FlightLog.objects.get(id=pk)
    except FlightLog.DoesNotExist:
        return Response({"error": "FlightLog not found"}, status=404)

    serializer = FlighLOgSerializer(obj, data=request.data)

    if serializer.is_valid():
        serializer.save()  
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete(request,pk):
    obj = FlightLog.objects.get(id=pk)
    obj.delete()
    return Response("logentry was deleted")
