import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def transform_weather_data(raw_data):
    """
    Transform raw weather data into a simplified format
    """
    logger.info("Transforming weather data")
    
    try:
        transformed = {
            "city": raw_data.get("name", ""),
            "country": raw_data.get("sys", {}).get("country", ""),
            "timestamp": datetime.utcfromtimestamp(raw_data.get("dt", 0)).strftime('%Y-%m-%d %H:%M:%S'),
            "temperature_c": raw_data.get("main", {}).get("temp", 0),
            "feels_like_c": raw_data.get("main", {}).get("feels_like", 0),
            "humidity": raw_data.get("main", {}).get("humidity", 0),
            "wind_speed": raw_data.get("wind", {}).get("speed", 0),
            "weather_condition": raw_data.get("weather", [{}])[0].get("description", ""),
            "cloudiness": raw_data.get("clouds", {}).get("all", 0)
        }
        
        # Calculate some aggregations
        transformed["temp_feels_diff"] = transformed["temperature_c"] - transformed["feels_like_c"]
        
        logger.info("Successfully transformed weather data")
        return transformed
    except Exception as e:
        logger.error(f"Error transforming weather data: {e}")
        raise

if __name__ == "__main__":
    # For testing the transformation locally
    test_data = {
        "name": "London",
        "sys": {"country": "GB"},
        "dt": 1686146400,
        "main": {
            "temp": 18.5,
            "feels_like": 17.8,
            "humidity": 65
        },
        "wind": {"speed": 3.1},
        "weather": [{"description": "scattered clouds"}],
        "clouds": {"all": 40}
    }
    transformed = transform_weather_data(test_data)
    print(transformed)