from django.shortcuts import render

# Create your views here.
import requests
import json
from datetime import datetime


def call_weather_sofia():
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': 42.698334,
            'lng': 23.319941,
            'params': ','.join(
                ['airTemperature', 'windSpeed', 'windDirection', 'visibility',
                 'humidity'])

        },
        headers={
            'Authorization': '756372fe-9bee-11ed-a138-0242ac130002-756373bc-9bee-11ed-a138-0242ac130002'
        }
    )

    # Do something with response data.
    json_data = response.json()

    with open("json/sofia_weather.json", "w") as f:
        f.writelines(json.dumps(json_data, indent=4, sort_keys=True))


def call_weather_gabrovo():
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': 42.874221,
            'lng': 25.318684,
            'params': ','.join(
                ['airTemperature', 'windSpeed', 'windDirection', 'visibility',
                 'humidity'])

        },
        headers={
            'Authorization': '756372fe-9bee-11ed-a138-0242ac130002-756373bc-9bee-11ed-a138-0242ac130002'
        }
    )

    # Do something with response data.
    json_data = response.json()

    with open("json/gabrovo_weather.json", "w") as f:
        f.writelines(json.dumps(json_data, indent=4, sort_keys=True))


def call_weather_varna():
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': 43.204666,
            'lng': 27.910543,
            'params': ','.join(
                ['airTemperature', 'windSpeed', 'windDirection', 'visibility',
                 'humidity'])

        },
        headers={
            'Authorization': '756372fe-9bee-11ed-a138-0242ac130002-756373bc-9bee-11ed-a138-0242ac130002'
        }
    )

    # Do something with response data.
    json_data = response.json()

    with open("json/varna_weather.json", "w") as f:
        f.writelines(json.dumps(json_data, indent=4, sort_keys=True))


def open_json_file(name_file="gabrovo_weather1"):
    with open(f"json/{name_file}.json") as file:
        return json.load(file)


def home(request):
    # api_information = call_weather_sofia(), call_weather_varna(), call_weather_gabrovo()

    return render(request, "weather_app/home.html", {})


def get_current_time():
    current_time = datetime.now().hour

    return current_time


def read_from_json(current_time=get_current_time(), name_file=""):
    from jsonpath_ng import jsonpath, parse

    current_time += 3
    json_data = open_json_file(name_file=name_file)

    jsonpath_expression_temp = parse(
        f'$.hours[{current_time}].airTemperature.noaa')
    jsonpath_expression_humidity = parse(
        f'$.hours[{current_time}].humidity.noaa')
    jsonpath_expression_visibility = parse(
        f'$.hours[{current_time}].visibility.noaa')
    jsonpath_expression_wind_direction = parse(
        f"$.hours[{current_time}].windDirection.noaa")

    temperature = jsonpath_expression_temp.find(json_data)

    humidity = jsonpath_expression_humidity.find(json_data)
    visibility = jsonpath_expression_visibility.find(json_data)
    wind_direction = jsonpath_expression_wind_direction.find(json_data)
    if temperature and humidity and visibility and wind_direction:
        temperature = temperature[0].value
        humidity = humidity[0].value
        visibility = visibility[0].value
        wind_direction = wind_direction[0].value
    else:
        temperature = 0
        humidity = 0
        visibility = 0
        wind_direction = 0

    return temperature, humidity, visibility, wind_direction


def show_sofia(request):
    temperature, humidity, visibility, wind_direction = read_from_json(
        name_file="sofia_weather")
    context = {"city": "Sofia", "temp": temperature, "humidity": humidity,
               "visibility": visibility, "winDir": wind_direction}
    return render(request, "weather_app/show_weather.html", context)


def show_varna(request):
    temperature, humidity, visibility, wind_direction = read_from_json(
        name_file="varna_weather")
    context = {"city": "Varna", "temp": temperature, "humidity": humidity,
               "visibility": visibility, "winDir": wind_direction}
    return render(request, "weather_app/show_weather.html", context)


def show_gabrovo(request):
    temperature, humidity, visibility, wind_direction = read_from_json(
        name_file="gabrovo_weather")
    context = {"city": "Gabrovo", "temp": temperature, "humidity": humidity,
               "visibility": visibility, "winDir": wind_direction}
    return render(request, "weather_app/show_weather.html", context)
