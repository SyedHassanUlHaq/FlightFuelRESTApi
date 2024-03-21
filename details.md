# FlightFuelRESTApi

This document outlines the structure and functionality of this project designed to manage airplanes using a RESTful API.

## `models.py`

- **Airplane Model**: Defines an `Airplane` model with two main fields:
  - `airplane_id`: An integer that uniquely identifies an airplane.
  - `passengers`: An integer representing the number of passengers on the airplane.

- **Dynamic Properties**:
  - `@property` `fuel_tank_capacity`: Calculates the fuel tank capacity based on the `airplane_id`. The capacity is calculated as 200 times the `airplane_id`.
  - `@property` `fuel_consumption_per_minute`: Calculates the base fuel consumption per minute (excluding the effect of passengers) using the logarithm of `airplane_id` multiplied by 0.80.

## `serializers.py`

- Utilizes Django REST Framework's `ModelSerializer` to create a serializer for the `Airplane` model.
- Specifies that the serialization process includes only the `airplane_id` and `passengers` fields of the `Airplane` model. This serializer facilitates the conversion between JSON data in HTTP requests/responses and `Airplane` model instances.

## `views.py`

- **AirplaneAPIView Class**: Inherits from DRF's `APIView` and is designed to handle HTTP requests.

  ### GET Request
  - Fetches all `Airplane` instances, serializes them using `AirplaneSerializer`, and returns the serialized data as JSON. This enables clients to retrieve a list of all airplanes in the database.

  ### POST Request
  - Handles the creation of a new `Airplane` instance. Accepts JSON data containing `airplane_id` and `passengers`, then uses `AirplaneSerializer` to validate and create a new `Airplane` object.
  - After creating the airplane, it calculates additional properties such as the total fuel consumption per minute (considering the effect of passengers) and the maximum minutes the airplane can fly based on its fuel capacity and consumption. These calculated details are then returned as JSON to the client.
  - The method accounts for the additional fuel consumption per passenger (0.002 units per minute per passenger) when calculating total fuel consumption, using properties defined in the model (`fuel_tank_capacity` and `fuel_consumption_per_minute`).
  - If the data provided in a POST request is invalid according to the serializer, the response includes a 400 status code and details about the error.
