import time
import paho.mqtt.client as mqtt

server = "localhost"
port = 1881
vhost = "yourvhost"
username = "username"
password = "password"
topic = "test/any"

try:
    client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
    client.username_pw_set(vhost + ":" + username, password)
    client.connect(server, port, keepalive=60, bind_address="") #connect
    client.loop_start() #start loop
    msgNum = int(input("Quantity of test messages: "))
    for i in range(msgNum):
        message = "test msg " + str(i + 1)
        client.publish(topic, payload=message, qos=1, retain=False) #publish
        time.sleep(1)
    client.loop_stop()  #stop loop
    client.disconnect()
except Exception, e:
    print e
