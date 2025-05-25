# test_etl.py
import extract
import transform
import pandas as pd

def test_api_response():
    data = extract.extract_data()
    assert isinstance(data, list)
    assert len(data) > 0

def test_transformation():
    sample = [{"name": {"common": "Egypt"}, "region": "Africa", "population": 100000000}]
    df = transform.transform_data(sample)
    assert isinstance(df, pd.DataFrame)
    assert "region" in df.columns
    assert "population" in df.columns
