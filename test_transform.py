import pytest
from transform import transform_weather_data
from datetime import datetime

def test_transform_weather_data():
    test_data = {
        "name": "Paris",
        "sys": {"country": "FR"},
        "dt": 1686146400,
        "main": {
            "temp": 22.3,
            "feels_like": 21.5,
            "humidity": 60
        },
        "wind": {"speed": 2.5},
        "weather": [{"description": "clear sky"}],
        "clouds": {"all": 10}
    }
    
    result = transform_weather_data(test_data)
    
    assert result["city"] == "Paris"
    assert result["country"] == "FR"
    assert result["temperature_c"] == 22.3
    assert result["feels_like_c"] == 21.5
    assert result["temp_feels_diff"] == pytest.approx(0.8)
    assert result["weather_condition"] == "clear sky"
    assert isinstance(result["timestamp"], str)