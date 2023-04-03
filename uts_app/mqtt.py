import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_temperature(client, userdata, msg):
    temp = Sensor.objects.get(name="temperature")
    temp.value = msg.payload.decode('utf-8')
    temp.save()
    temp_log = SensorLog(name=temp, value=msg.payload.decode('utf-8'))
    temp_log.save()
    print('Received a new temperature data ', msg.payload.decode('utf-8'))   
    
def on_message_friction(client, userdata, msg):
    fric = Sensor.objects.get(name="friction")
    fric.value = msg.payload.decode('utf-8')
    fric.save()
    fric_log = SensorLog(name=fric, value=msg.payload.decode('utf-8'))
    fric_log.save()
    print('Received a new friction data ', msg.payload.decode('utf-8'))   
    
     
def on_message_power(client, userdata, msg):
    power = Sensor.objects.get(name="power")
    power.value = msg.payload.decode('utf-8')
    power.save()
    power_log = SensorLog(name=power, value=msg.payload.decode('utf-8'))
    power_log.save()
    print('Received a new power data ', msg.payload.decode('utf-8'))    

def on_connect(client, userdata, rc, result):
    client.subscribe('uts/#')

client = mqtt.Client()
client.message_callback_add('uts/temperature', on_message_temperature)
client.message_callback_add('uts/friction', on_message_friction)
client.message_callback_add('uts/power', on_message_power)
client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
