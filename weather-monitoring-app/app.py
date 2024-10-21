from flask import Flask, jsonify, send_from_directory, send_file
from weather_api import get_weather_for_all_cities
from processing import process_weather_data
from db import init_db, save_daily_summary
from visualize import create_visualization
from alerting import check_and_alert
import os
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Route for the homepage ('/')
@app.route('/')
def home():
    return "Welcome to the Weather Monitoring App!"

# Route to fetch weather data
@app.route('/get-weather', methods=['GET'])
def fetch_weather():
    data = get_weather_for_all_cities()
    logging.info("Fetched weather data: %s", data)  # Debugging log
    daily_summary = process_weather_data(data)
    logging.info("Processed weather summary: %s", daily_summary)  # Debugging log
    save_daily_summary(daily_summary)
    check_and_alert(data)
    return jsonify(daily_summary)

# Route for visualizing weather data
@app.route('/visualize', methods=['GET'])
def visualize():
    image_path = create_visualization()  
    return send_file(image_path, mimetype='image/png')

# Route to handle requests for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Route to check alerts
@app.route('/check-alerts', methods=['GET'])
def check_alerts():
    try:
        # Get the latest weather data for all cities
        data = get_weather_for_all_cities()
        print("Weather Data:", data)  # Debugging output

        # Call the check_and_alert function with the weather data
        alerts = check_and_alert(data)
        print("Alerts:", alerts)  # Debugging output

        # Return alerts as a JSON response
        return jsonify(alerts)
    except Exception as e:
        # Log the error and return a 500 Internal Server Error response
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    logging.info("Initializing database...")
    init_db()
    logging.info("Starting Flask application...")
    app.run(debug=True)
