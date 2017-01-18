import time
import paho.mqtt.client as mqtt
from random import randint
from string import ascii_uppercase
import random, string
from itertools import islice

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))


server = "localhost"
port = 1881
vhost = "yourvhost"
username = "username"
password = "password"
topic = "test"

try:
    client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
    client.username_pw_set(vhost + ":" + username, password)
    client.connect(server, port, keepalive=60, bind_address="") #connect
    client.loop_start() #start loop
    msgNum = int(input("Quantity of Node to be added to users randomly: "))
    for i in range(msgNum):
        random_gen = randomword(12)
        User_id = 1
        print(random_gen)
        message = random_gen +"/" + str(User_id)
        client.publish(topic, payload=message, qos=0, retain=False) #publish
        time.sleep(1)
    client.loop_stop()  #stop loop
    client.disconnect()
except Exception, e:
    print e
