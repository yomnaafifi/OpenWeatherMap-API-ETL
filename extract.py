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
    data = extract_data()
    # ✅ This line makes sure raw_data.json gets valid content
    print(json.dumps(data))
