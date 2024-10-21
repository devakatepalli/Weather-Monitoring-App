# Weather Monitoring App

Welcome to the Weather Monitoring App! This application allows users to fetch real-time weather data for multiple cities, visualize this data, and set up alert notifications for extreme weather conditions.

## Features
- Fetch real-time weather data for selected cities.
- Process and store daily weather summaries in a database.
- Send email alerts for extreme weather conditions.
- Visualize weather data through graphical representations.
- Check and manage alerts via a dedicated endpoint.

## Technologies Used
- **Flask**: A micro web framework for Python.
- **SQLite**: Lightweight database to store weather summaries and alerts.
- **Requests**: For making API calls to the OpenWeatherMap API.
- **Matplotlib**: For creating visualizations of weather data.
- **SmtpLib**: For sending email alerts.

## Directory Structure

Here’s a brief overview of the project directory structure:
/weather-monitoring-app ├── app.py  ├── weather_api.py  ├── processing.py  ├── db.py  ├── visualize.py  ├── alerting.py   ├── tests/ │ ├── test_weather_api.py  │ └── test_processing.py 
├── requirements.txt  ├── config.py  └── static

## Setup Instructions

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.13**: Download and install from [python.org](https://www.python.org/).
- **Required Python packages**: Listed in `requirements.txt`.

## Installation Steps
1. Navigate to the Project Directory:

      cd weather-monitoring-app
   
2. Install Required Packages:

      pip install -r requirements.txt
       ( Flask, 
         Pandas,
         Requests,
         Matplotlib)


3. Set Up Environment Variables:

   Create a config.py file in the project directory or set environment variables for your email settings and OpenWeather API key.

4. Initialize the Database:

   Run the application to set up the database:

   python app.py  # or simply run flask run if set up properly

## Endpoints
1. Home Page:

        URL: /
        Method: GET
        Description: Displays a welcome message.
        Expected Response: Welcome to the Weather Monitoring App!

2. Fetch Weather Data:
   
        URL: /get-weather
        Method: GET
        Description: Fetches weather data for configured cities and returns a summary of the daily weather conditions.
        Expected Response: A JSON object containing the weather summary.
   
3. Visualize Weather Data

        URL: /visualize
        Method: GET
        Description: Generates and serves a visualization of the weather data as a PNG image.
        Expected Response: A PNG image of the weather visualization.
   
4. Check Alerts

        URL: /check-alerts
        Method: GET
        Description: Checks for any weather alerts based on the fetched weather data and returns them.
        Expected Response: A JSON object containing any active alerts.

## Usage
1. Start the Flask Server:

      flask run
   
2. Access the Application:
      Open your browser and navigate to http://127.0.0.1:5000/ to access the application.

### Fetch Weather Data
curl "http://127.0.0.1:5000/get-weather"

### Visualize Weather Data
curl "http://127.0.0.1:5000/visualize"

### Check Alerts
curl "http://127.0.0.1:5000/check-alerts"
