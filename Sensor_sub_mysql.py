#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb as mdb
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
from random import randint
from string import ascii_uppercase
from itertools import islice
import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

server = "localhost"
port = 1881
vhost = "yourvhost"
username = "username1"
password = "password"
topic = "AddSensor/#"
con = mdb.connect('localhost', 'root', '  ', 'test')

"""
 * This method is the callback on connecting to broker.
 * @ It subscribes the target topic.
"""
def onConnect(client, userdata, rc):    #event on connecting
    client.subscribe([(topic, 1)])  #subscribe

"""
 * This method is the callback on receiving messages.
 * @ It prints the message topic and payload on console.
"""
def onMessage(client, userdata, message):   #event on receiving message
    print("Topic: " + message.topic + ", Message: " + message.payload )

    with con:
	# For random DOC
        var = randint(0,365)
        doc = datetime.now()-timedelta(365-var)
        description = randomword(12)
        data = message.topic.split("/")
        print (message.payload)
        cur = con.cursor()
        cur.execute("INSERT INTO chain_sensor (name, node_name_id, doc, description) " "VALUES ('{0}','{1}','{2}','{3}')" .format(message.payload,
	int(data[1]), doc, description))

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
