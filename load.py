import pandas as pd
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def save_to_csv(data, filename="weather_data.csv"):
    """
    Save transformed data to a CSV file
    """
    try:
        # Convert to DataFrame
        df = pd.DataFrame([data])
        
        # Check if file exists to append or create new
        if os.path.exists(filename):
            # Append to existing file
            df.to_csv(filename, mode='a', header=False, index=False)
            logger.info(f"Appended data to existing file: {filename}")
        else:
            # Create new file
            df.to_csv(filename, index=False)
            logger.info(f"Created new file with data: {filename}")
    except Exception as e:
        logger.error(f"Error saving data to CSV: {e}")
        raise

if __name__ == "__main__":
    # For testing the loading locally
    test_data = {
        "city": "London",
        "country": "GB",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "temperature_c": 18.5,
        "feels_like_c": 17.8,
        "humidity": 65,
        "wind_speed": 3.1,
        "weather_condition": "scattered clouds",
        "cloudiness": 40,
        "temp_feels_diff": 0.7
    }
    save_to_csv(test_data)