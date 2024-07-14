from flask import render_template, request
import requests
from . import create_app

app = create_app()

@app.route('/home', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            api_key = app.config['WEATHER_API_KEY']
            response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
            weather_data = response.json()
    return render_template('index.html', weather=weather_data)
