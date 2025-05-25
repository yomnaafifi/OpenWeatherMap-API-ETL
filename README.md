# OpenWeatherMap ETL Pipeline 🌦️📊

A lightweight ETL pipeline that extracts daily weather data from the OpenWeatherMap API, transforms it, and stores it as CSV. Automated via GitHub Actions.

---

## Features

- **Extract**: Fetches weather data (temperature, humidity, etc.) from OpenWeatherMap API.
- **Transform**: Cleans data and calculates aggregates (e.g., temp-feels-like difference).
- **Load**: Saves processed data to `weather_data.csv`.
- **Automated**: Runs daily via GitHub Actions.
- **Secure**: Uses GitHub Secrets for API keys.

---

## Quick Start

1. **Clone the repo:**
    ```bash
    git clone https://github.com/yomnaafifi/OpenWeatherMap-API-ETL.git
    ```

2. **Set up environment:**
    - Add your OpenWeatherMap API key to GitHub Secrets (`OPENWEATHER_API_KEY`),  
      **or** create a `.env` file locally:
      ```
      OPENWEATHER_API_KEY=your_api_key_here
      ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run manually:**
    ```bash
    python extract.py && python transform.py && python load.py
    ```

---

## Workflow Overview

```mermaid
graph LR
     A[GitHub Actions] -->|Daily| B(Extract)
     B --> C(Transform)
     C --> D(Load to CSV)
     D --> E(Upload Artifact)
```

---

## File Structure

```
├── .github/workflows/
│   └── etl.yml            # Scheduled workflow
├── src/
│   ├── extract.py         # API data extraction
│   ├── transform.py       # Data processing
│   └── load.py            # CSV export
├── tests/                 # pytest validation
├── requirements.txt       # Dependencies
└── weather_data.csv       # Sample output
```

---

## Customize

- **Change target city:** Edit `src/extract.py`.
- **Modify transformations:** Edit `src/transform.py`.
- **Adjust schedule:** Edit `.github/workflows/etl.yml`.

---

## Requirements

- Python 3.9+
- OpenWeatherMap API key (free tier)
