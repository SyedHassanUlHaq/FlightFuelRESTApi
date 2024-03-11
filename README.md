# FlightFuelRESTApi

## Project Overview

FlightFuelRESTApi is a RESTful API developed  to optimize and manage airplane fuel consumption and flight capacities. Utilizing Django and Django REST Framework, this project adheres to RESTful principles, offering a scalable and efficient way to calculate fuel requirements and flight durations based on varying airplane and passenger configurations.

## Installation

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)

### Setup

1. **Clone The Repository**:
```bash
git clone https://github.com/SyedHassanUlHaq/FlightFuelRESTApi.git
cd FlightFuelRESTApi/kami_airlines
```

2. **Run Migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Start The Server:**
```bash
python manage.py runserver
```

## Usage

### Endpoints

- **Create Airplane**:
  - **POST** `/api/airplanes/`
    - **Input**: `{ "airplane_id": int, "passengers": int }`
    - **Output**: Details including fuel consumption and max minutes able to fly.

- **List Airplanes**:
  - **GET** `/api/airplanes/`
    - **Output**: List of all airplanes with their details.

### Sample Request (using curl)

- **Create Airplane**:

```bash
  curl -X POST http://localhost:8000/api/airplanes/ -d "airplane_id=1&passengers=100"
```

## List Airplanes

To list all airplanes, use the following `curl` command:

```bash
curl http://localhost:8000/api/airplanes/
```

## Testing

To run the tests and generate a coverage report, follow these steps:

### Run Tests

Execute the following command to run the tests:

```bash
python manage.py test
```

### Measure Coverage 

First, ensure you have coverage installed. If not, install it using pip:

```bash
pip install coverage
```

Then, run the tests with coverage measurement:
```bash
coverage run --source='.' manage.py test
coverage report
```
