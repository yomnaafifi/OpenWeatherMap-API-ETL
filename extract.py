import requests
import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def fetch_weather_data(city="London"):
    """
    Fetch weather data from OpenWeatherMap API
    """
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        logger.error("OPENWEATHER_API_KEY not found in environment variables")
        raise ValueError("API key missing")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        logger.info(f"Fetching weather data for {city}")
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        logger.info("Successfully fetched weather data")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        raise

if __name__ == "__main__":
    # For testing the extraction locally
    data = fetch_weather_data()
    print(data)