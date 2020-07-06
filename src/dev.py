from fronius_to_influx import FroniusToInflux
from influxdb import InfluxDBClient
from astral import Location

import pytz


client = InfluxDBClient(host='localhost', port=8086, username='', password='', ssl=False)
client.switch_database('Fronius')
location = Location(('Poznan', 'Europe', 52.408078, 16.933618, 'Europe/Warsaw', 87))
tz = pytz.timezone('Europe/Warsaw')
endpoints = [
    'http://127.0.0.1:5000/3PInverterData.json',
    'http://127.0.0.1:5000/CommonInverterData.json',
    'http://127.0.0.1:5000/MinMaxInverterData.json'
]

z = FroniusToInflux(client, location, endpoints, tz)
z.IGNORE_SUN_DOWN = True
z.run()
