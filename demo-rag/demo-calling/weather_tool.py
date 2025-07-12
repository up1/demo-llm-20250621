import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

if __name__ == "__main__":
    lat = 40.7128  # Example latitude for New York City
    lon = -74.0060  # Example longitude for New York City
    temperature = get_weather(lat, lon)
    print(f"The current temperature at latitude {lat} and longitude {lon} is {temperature}°C.")