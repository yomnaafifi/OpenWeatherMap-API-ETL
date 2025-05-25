# load.py
import pandas as pd
import logging

logging.basicConfig(filename='etl.log', level=logging.INFO)

def load_data(df, path="data/output.csv"):
    df.to_csv(path, index=False)
    logging.info(f"Data written to {path}")
