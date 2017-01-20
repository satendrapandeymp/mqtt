#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports

import time
import MySQLdb as mdb
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
from random import randint
from string import ascii_uppercase
import random , string
from itertools import islice

# For connecting to mosquitto
server = "localhost"
port = 1881
vhost = "yourvhost"
username = "username"
password = "password"
topic = "sensor/#"

# For connection to mysql
con = mdb.connect('localhost', 'root', '  ', 'test')

# For subscribing our topic on connect
def onConnect(client, userdata, rc):    #event on connecting
    client.subscribe([(topic, 1)])  #subscribe

def onMessage(client, userdata, message):   #event on receiving message

    # For writing in database
    with con:

        # TODO floating point data insertion -- Done
	# TODO message payload -- data only -- Done -- Data+Doc
        
	# Split message to get data and sensor id Respectively
        Data = message.payload.split("/")
        sen = message.topic.split("/")

        # For Writing data in database
        # TODO Modify tables -- Remove description -- Data , Image -- Node/sensor -- Done

        print("Topic: " + message.topic + ", Message: " + message.payload )
        cur = con.cursor()
        cur.execute("INSERT INTO chain_data ( data,sensor_name_id, doc) " "VALUES ('{0}','{1}','{2}')" .format(float(Data[0]), int(sen[1]), Data[1]))

# for connection with mosquitto
while True:
    try:
        client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
        client.username_pw_set(vhost + ":" + username, password)
        client.on_connect = onConnect
        client.on_message = onMessage
        client.connect(server, port, keepalive=60, bind_address="12") #connect
        client.loop_forever()   #automatically reconnect once loop forever
    except Exception, e:
        #when initialize connection, reconnect on exception
        print "Exception handled, reconnecting...\nDetail:\n%s" % e
        time.sleep(5)
