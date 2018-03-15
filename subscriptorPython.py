import paho.mqtt.client as mqtt
import serial, time


#b = readline
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sensor/luminico")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(str(msg.payload)=='sectorD_1'):
        arduino = serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorD_1')
        arduino.close()
    if(str(msg.payload)=='sectorD_0'):
        arduino=serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorD_0')
        arduino.close()
    if(str(msg.payload)=='sectorC_1'):
        arduino = serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorC_1')
        arduino.close()
    if(str(msg.payload)=='sectorC_0'):
        arduino=serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorC_0')
        arduino.close()
    if(str(msg.payload)=='sectorB_1'):
        arduino = serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorB_1')
        arduino.close()
    if(str(msg.payload)=='sectorB_0'):
        arduino=serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorB_0')
        arduino.close()
    if(str(msg.payload)=='sectorA_1'):
        arduino=serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorA_1')
        arduino.close()
    if(str(msg.payload)=='sectorA_0'):
        arduino=serial.Serial("/dev/ttyUSB0", 9600)
        arduino.write(b'sectorA_0')
        arduino.close()



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.6", 1883, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
