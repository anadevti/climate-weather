import os

class Config:
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'your_api_key_here')
