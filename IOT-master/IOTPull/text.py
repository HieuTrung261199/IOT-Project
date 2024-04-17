import paho.mqtt.client as mqtt
import time

username = "Kx4yGAsGCCcGCw8cHRUrChs"
password = "0nc6Of4lUpg9AIfpGSYHC/C3"
ClientID = "Kx4yGAsGCCcGCw8cHRUrChs"
i = 0


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    channel_ID = "2271054"
    client.subscribe("channels/%s/subscribe/fields/field1"%(channel_ID))
    client.subscribe("channels/%s/subscribe/fields/field2"%(channel_ID))
    client.subscribe("channels/%s/subscribe/fields/field3"%(channel_ID))

def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")
    
    
def on_message(client, userdata, message):
    
    if message.topic == 'channels/2271054/subscribe/fields/field1':
        temp = message.payload.decode()[0:2]
        print("Nhiet do: {}".format(temp))
        
        if int(temp)>=20 and int(temp)<=30:
            print("Giu status")
        if int(temp)<20:
            print("1")
        if int(temp)>30:
            print("2")
    if message.topic == 'channels/2271054/subscribe/fields/field2':
        humi = message.payload.decode()[0:2]
        
        print("Do am: {}".format(humi))
        if int(humi)>=80 and int(humi)<=90:
            print("giu status")
        if int(humi)>90:
            print("3")
        if int(humi)<80:
            print("4")
    if message.topic == 'channels/2271054/subscribe/fields/field3':
        rd = message.payload.decode()[0:3]
        rds = rd

        print("Random: {}".format(rd))
        print('--------------------')
        if (int(rd) > 50):
            print("5s")
        else:
            print("76")
    
client = mqtt.Client(ClientID)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_forever()