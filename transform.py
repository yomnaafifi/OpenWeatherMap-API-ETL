# transform.py
import pandas as pd
import logging

logging.basicConfig(filename='etl.log', level=logging.INFO)

def transform_data(raw_data):
    countries = []
    for country in raw_data:
        countries.append({
            "name": country.get("name", {}).get("common"),
            "region": country.get("region"),
            "population": country.get("population", 0)
        })
    df = pd.DataFrame(countries)
    agg_df = df.groupby("region").agg({"population": "sum"}).reset_index()
    logging.info("Data transformed and aggregated")
    return agg_df
