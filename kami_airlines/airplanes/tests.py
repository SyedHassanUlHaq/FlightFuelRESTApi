from django.test import TestCase
from rest_framework.test import APIClient
from .models import Airplane

class AirplaneModelTests(TestCase):
    def test_fuel_tank_capacity(self):
        """Test the fuel tank capacity calculation."""
        airplane = Airplane(airplane_id=1)
        self.assertEqual(airplane.fuel_tank_capacity, 200)

    def test_fuel_consumption_per_minute(self):
        """Test the fuel consumption calculation without passengers
        
        Given that the fuel_consumption_per_minute calculation uses the logarithm of the airplane ID,
        and considering the properties of logarithmic functions, the result would indeed be problematic
        when airplane_id is 1 (since log(1) equals 0). This could lead to a failure in any test case
        expecting a positive value for fuel consumption when the airplane ID is exactly 1.
        """
        airplane = Airplane(airplane_id=2) # Choosing an ID > 1 to ensure a positive fuel consumption
        self.assertTrue(airplane.fuel_consumption_per_minute > 0)

class AirplaneAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_airplane(self):
        """Test creating an airplane through the API."""
        response = self.client.post('/api/airplanes/', {'airplane_id': 2, 'passengers': 100}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fuel_consumption_per_minute', response.data)
        self.assertIn('max_minutes_able_to_fly', response.data)

    def test_get_airplanes(self):
        """Test listing airplanes through the API."""
        response = self.client.get('/api/airplanes/')
        self.assertEqual(response.status_code, 200)
