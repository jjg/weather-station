import os
import time

from ambient_api.ambientapi import AmbientAPI

api = AmbientAPI(
)

devices = api.get_devices()
#print(devices)
device = devices[0]

time.sleep(1)

#print(device.get_data())

device_data = device.get_data(limit=1)
#print(device_data)
current_conditions = device_data[0]
print(f"Outdoor Temp: {current_conditions['tempf']}")
print(f"Outdoor Humidity: {current_conditions['humidity']}")
print(f"Windspeed: {current_conditions['windspeedmph']}")
print(f"Wind Direction: {current_conditions['winddir']}")
print(f"Pressure: {current_conditions['baromrelin']}")


