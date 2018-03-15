import paho.mqtt.client as paho
import serial, time
arduino= serial.Serial('/dev/ttyUSB0',9600)
def on_publish(client,userdata,mid):
	print("mid: "+str(mid))
client = paho.Client()
client.on_publish = on_publish
client.connect("127.0.0.1",1883)
client.loop_start()
while  True:
	arduino.close()
	arduino.open()
	leerString = arduino.readline()
	print leerString
	if leerString!="":
		
		(rc,mid)=client.publish("sensor/luminico",str(leerString),qos=1)
		arduino.close()
		time.sleep(0.5)
	arduino.close()
	time.sleep(0.5)
