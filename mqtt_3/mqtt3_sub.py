from paho.mqtt import client as mqtt_client


broker = "10.157.150.7"
port = 1883
topics = [("Topics/topsecret/info", 0),
          ("Topics/topsecret/alert", 0)]
topic = ", ".join([topics[i][0] for i in range(len(topics))])


def run():
    cl = mqtt_client.Client()
    cl.on_connect = lambda client, userdata, flags, rc: (
        print(f"Connected to MQTT Broker! Subscribed to topics '{topic}'!" if rc == 0 else f"Failed to connect, RC {rc}"))
    cl.on_message = lambda client, userdata, msg: (
        print(f"{msg.topic}:{' ' * (40 - len(msg.topic))}{msg.payload.decode()}"))
    cl.username_pw_set(username="sub_admin", password="Passw0rdADMIN99")
    cl.connect(broker, port)
    cl.subscribe(topics)
    cl.loop_forever()


run()
