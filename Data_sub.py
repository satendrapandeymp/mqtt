# Imports
import time
import paho.mqtt.client as mqtt
from random import randint
from string import ascii_uppercase
import random, string
from itertools import islice
from datetime import datetime, timedelta

# For generating random world string as data
def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

# For connection with mosquitto
server = "localhost"
port = 1881
vhost = "yourvhost"
username = "username"
password = "password"
topic = "sensor/"
# Unique topic

# connecting to mosquitto
try:
    client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
    client.username_pw_set(vhost + ":" + username, password)
    client.connect(server, port, keepalive=60, bind_address="") #connect
    client.loop_start() #start loop

    # For number of data to generate randomly
    msgNum = int(input("Quantity of data: "))
    for i in range(msgNum):

        # For generation of random String to treat as data
        random_gen = random.uniform(4.5, 42.7)
        print(random_gen)

        # I had already set 1001 sensors so chossing a random sensor to put data in that sensor's table
        sensor_id = randint(1,10)
        topic = "sensor/"
        topic += str(sensor_id) + "/data/"
        # For setting a random DOC.
        var = randint(0,365)
        doc = datetime.now()-timedelta(365-var)


        # Joining data and Sensor_id with "/" so we can break it and get data and sensor id seperate to write data
        message = str(random_gen) + "/" + str(doc)

        # timestamp 1072392329
        # data 1239002382

        #publish
        client.publish(topic, payload=message, qos=0, retain=False)

        # Sleeping for .0001 sec
        time.sleep(.0001)

    # stop loop
    client.loop_stop()

    # disconnecting
    client.disconnect()

# Printing in case of errors
except Exception, e:
    print e
