from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer

class AirplaneAPIView(APIView):
    def get(self, request):
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            airplane = serializer.save()
            fuel_capacity = airplane.fuel_tank_capacity
            base_fuel_consumption_per_minute = airplane.fuel_consumption_per_minute
            total_fuel_consumption_per_minute = base_fuel_consumption_per_minute + airplane.passengers * 0.002
            max_minutes_able_to_fly = fuel_capacity / total_fuel_consumption_per_minute
            
            response_data = {
                'airplane_id': airplane.airplane_id,
                'passengers': airplane.passengers,
                'fuel_consumption_per_minute': total_fuel_consumption_per_minute,
                'max_minutes_able_to_fly': max_minutes_able_to_fly,
            }
            return Response(response_data)
        return Response(serializer.errors, status=400)
