import pytest
from unittest.mock import patch, Mock
from extract import fetch_weather_data
import os
import pytest
from unittest.mock import patch, Mock
import requests  # Required for HTTPError

@patch('extract.requests.get')
def test_fetch_weather_data_success(mock_get):
    # Setup mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "London", "weather": [{"description": "cloudy"}]}
    mock_get.return_value = mock_response
    
    # Test with mock API key
    with patch.dict(os.environ, {"OPENWEATHER_API_KEY": "test_key"}):
        result = fetch_weather_data()
        
    assert result["name"] == "London"
    assert "weather" in result

@patch('extract.requests.get')
def test_fetch_weather_data_failure(mock_get):
    # Setup mock failed response
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
    mock_get.return_value = mock_response
    
    with patch.dict(os.environ, {"OPENWEATHER_API_KEY": "test_key"}):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            fetch_weather_data()
        assert "404 Client Error" in str(exc_info.value)