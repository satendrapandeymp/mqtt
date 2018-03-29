import paho.mqtt.client as mqtt, time

try:
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.loop_start() #start loop
    topic = "sensor/pandey"

    time1 = time.time()
    f=open("test.jpg", "rb") #3.7kiB in same folder
    fileContent = f.read()
    message = bytearray(fileContent)
    print time.time() - time1

    client.publish(topic, payload=message, qos=0, retain=False)

    client.loop_stop()
    client.disconnect()

# Printing in case of errors
except Exception, e:
    print e
