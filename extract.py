import requests
import logging
import json

logging.basicConfig(filename='etl.log', level=logging.INFO)

def extract_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        logging.info("Data extracted successfully")
        return response.json()
    else:
        logging.error(f"API Request Failed: {response.status_code}")
        raise Exception("Failed to fetch data")

if __name__ == "__main__":
    try:
        data = extract_data()
        # ✅ Print valid JSON so it gets saved into raw_data.json
        print(json.dumps(data))
    except Exception as e:
        logging.error(str(e))
        print("[]")  # Return an empty JSON list to prevent crash
