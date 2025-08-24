import requests
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# OpenWeatherMap API configuration
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def extract_city(user_input):
    """Extract city name from user input using spaCy NER."""
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # GPE = Geo-Political Entity (cities, countries)
            return ent.text
    return None

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"]
        }
        return weather
    else:
        return None

def main():
    print("WeatherBot: Hi! Ask me about the weather in any city.")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("WeatherBot: Goodbye!")
            break
        city = extract_city(user_input)
        if not city:
            print("WeatherBot: Sorry, I couldn't find a city in your question. Please try again.")
            continue
        weather = get_weather(city)
        if weather:
            print(f"WeatherBot: Weather in {weather['city']}:")
            print(f"  Temperature: {weather['temp']}°C")
            print(f"  Condition: {weather['condition']}")
            print(f"  Humidity: {weather['humidity']}%")
        else:
            print("WeatherBot: Sorry, I couldn't fetch the weather for that city. Please check the city name.")

if __name__ == "__main__":
    main()