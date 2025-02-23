import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Step 1: Fetch data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.json().get('message', 'Unknown error')}")
        return None

# Step 2: Process data for visualization
def process_weather_data(data):
    timestamps = []
    temperatures = []
    weather_descriptions = []

    for entry in data["list"]:
        timestamps.append(datetime.datetime.fromtimestamp(entry["dt"]))
        temperatures.append(entry["main"]["temp"])
        weather_descriptions.append(entry["weather"][0]["description"])

    return timestamps, temperatures, weather_descriptions

# Step 3: Visualize data using Matplotlib and Seaborn
def visualize_weather_data(timestamps, temperatures, weather_descriptions):
    sns.set(style="whitegrid")
    
    # Line plot for temperature trend
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, temperatures, marker="o", linestyle="-", color="b", label="Temperature (°C)")
    plt.title("Temperature Trend in Mumbai", fontsize=16)
    plt.xlabel("Date/Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Bar plot for temperatures
    plt.figure(figsize=(12, 6))
    sns.barplot(x=timestamps, y=temperatures, palette="coolwarm")
    plt.title("Temperature Distribution in Mumbai", fontsize=16)
    plt.xlabel("Date/Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main Function to Execute the Script
if __name__ == "__main__":
    # City and API Key
    city = "Mumbai"
    api_key = "94a0a4e1b288e38fe7ba27dd0f05b933"

    # Fetch and process weather data
    data = fetch_weather_data(city, api_key)
    if data:
        timestamps, temperatures, weather_descriptions = process_weather_data(data)

        # Visualize the data
        visualize_weather_data(timestamps, temperatures, weather_descriptions)
