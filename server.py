from flask import Flask, request, jsonify
import requests
import os
import threading


app = Flask(__name__)


GEOLOCATION_API_KEY = "your_geolocation_api_key"
FASHION_API_URL = "https://fashion-api.com/trends"  # Replace with the actual fashion API URL

def get_location(ip_address):
    # Mock response for demonstration purposes
    return {"city": "New York"}

def get_fashion_trends(location):
    # Mock fashion trends based on location
    trends = {
        "New York": ["Streetwear", "Designer Brands"],
        "Tokyo": ["Harajuku", "Kimono"],
        "Paris": ["Haute Couture", "Chic"],
        # Add more locations and trends
    }
    return trends.get(location, ["Global Trends"])

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_ip = request.remote_addr  # Get the user's IP address
    location_data = get_location(user_ip)
    location = location_data.get("city", "Global")

    trends = get_fashion_trends(location)

    response = {
        "location": location,
        "fashion_trends": trends,
        "message": f"Hello! Based on your location in {location}, here are the latest fashion trends: {', '.join(trends)}"
    }
    return jsonify(response)

def run_app():
    app.run(host='0.0.0.0', port=5000)

thread = threading.Thread(target=run_app)
thread.start()




from flask import Flask, request, jsonify
import requests
import threading
import os

app = Flask(__name__)


GEOLOCATION_API_KEY = os.getenv("GEOLOCATION_API_KEY", "your_geolocation_api_key")
FASHION_API_URL = "https://fashion-api.com/trends"  # Replace with the actual fashion API URL

def get_location(ip_address):
    response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={GEOLOCATION_API_KEY}&ip={ip_address}")
    return response.json()

def get_fashion_trends(location):
    # Mock fashion trends based on location
    trends = {
        "New York": ["Streetwear", "Designer Brands"],
        "Tokyo": ["Harajuku", "Kimono"],
        "Paris": ["Haute Couture", "Chic"],
        # Add more locations and trends
    }
    return trends.get(location, ["Global Trends"])

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_ip = request.remote_addr  # Get the user's IP address
    location_data = get_location(user_ip)
    location = location_data.get("city", "Global")

    trends = get_fashion_trends(location)

    response = {
        "location": location,
        "fashion_trends": trends,
        "message": f"Hello! Based on your location in {location}, here are the latest fashion trends: {', '.join(trends)}"
    }
    return jsonify(response)

# Function to run the Flask app
def run_app():
    app.run(host='0.0.0.0', port=5000)


threading.Thread(target=run_app).start()