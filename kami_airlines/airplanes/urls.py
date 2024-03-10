from django.urls import path
from .views import AirplaneAPIView

urlpatterns = [
    path('airplanes/', AirplaneAPIView.as_view(), name='airplanes-api'),
]