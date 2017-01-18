#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb as mdb
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
from random import randint
from string import ascii_uppercase
import random
from itertools import islice

def random_chars(size, chars=ascii_uppercase):
    selection = iter(lambda: random.choice(chars), object())
    while True:
        yield ''.join(islice(selection, size))

server = "localhost"
port = 1881
vhost = "yourvhost"
username = "username1"
password = "password"
topic = "test"
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
    #temp = message.payload
    #print(temp)
    #print(temp.split(',')[0], temp.split(',')[1])
    with con:
        var = randint(0,365)
        doc = datetime.now()-timedelta(365-var)
        random_gen = random_chars(12)
        Data = message.payload.split("/")
        cur = con.cursor()
        cur.execute("INSERT INTO chain_node (name, owner_id, doc, description) " "VALUES ('{0}',{1},'{2}','{3}')" .format(Data[0], int(Data[1]), doc, random_gen))

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
