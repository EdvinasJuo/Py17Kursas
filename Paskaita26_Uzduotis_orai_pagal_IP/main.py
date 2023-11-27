import requests
import ipbase
import csv

def get_city_from_ip(ip_address):
    client = ipbase.Client('ipb_live_NcF4d7WoLJmEYzsc35x1ICyZGJU1mH3oWfcDgLyX')
    result = client.info(ip_address)

    if result and 'data' in result:
        country_info = result['data']['location']['country']
        country = country_info.get('name_translated')
        city_info = result['data']['location']['city']
        city = city_info.get('name_translated')
        latitude = result['data']['location']['latitude']
        longitude = result['data']['location']['longitude']

        # SUFORMATUOTA, KAD GAUTI DU SKAICIUS PO KABLELIO
        latitude = "{:.2f}".format(latitude)
        longitude = "{:.2f}".format(longitude)

        return ip_address, country, city, latitude, longitude
    else:
        return ip_address, "IP not found or error occurred", None, None, None


def get_temp_and_weather_by_latitude_and_longtitude():
    api_key = 'b3abd2280965461b01c6d25319b87816'
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(weather_api)

    if response.status_code == 200:
        data = response.json()  # Konvertuojame gautus duomenis iš API į žodyną

        temp_kelvin = data['main']['temp']
        temperature_to_celsius = temp_kelvin - 273.15

        weather = data['weather'][0]['main']

        return int(temperature_to_celsius), weather

    else:
        print(f'Klaida gavus atsakymą iš API. Statuso kodas: {response.status_code}')
        return None


def writing_in_csv(weather_data, filename):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(["IP", "Country", "City", "Temp", "Weather"])
        for row in weather_data:
            writer.writerow(row)


ip_list = ['122.35.203.161',
           '174.217.10.111',
           '187.121.176.91',
           '176.114.85.116',
           '174.59.204.133',
           '54.209.112.174',
           '109.185.143.49',
           '176.114.253.216',
           '210.171.87.76',
           '24.169.250.142'
           ]

weather_data = []

for ip_address in ip_list:
    ip, country, city, latitude, longitude = get_city_from_ip(ip_address)
    temperature, weather = get_temp_and_weather_by_latitude_and_longtitude()
    weather_data.append([ip, country, city, temperature, weather])
    print(f"IP: {ip}, Country: {country}, City: {city}, Temp: {temperature}, Weather: {weather}")

get_temp_and_weather_by_latitude_and_longtitude()
writing_in_csv(weather_data, "orai_12.csv")
