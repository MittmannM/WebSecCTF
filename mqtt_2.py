from paho.mqtt import client as mqtt_client


broker = "10.157.150.7"
port = 1883
topic = "Topics/default/flag_4_you"


def run():
    cl = mqtt_client.Client()
    cl.on_connect = lambda client, userdata, flags, rc: (
        print(f"Connected to MQTT Broker! Subscribed to topic '{topic}'!" if rc == 0 else f"Failed to connect, RC {rc}"))
    cl.on_message = lambda client, userdata, msg: (
        print(f"{msg.topic}:{' ' * (40 - len(msg.topic))}{msg.payload.decode()}"))
    cl.username_pw_set(username="sub_admin", password="Passw0rdADMIN99")
    cl.connect(broker, port)
    cl.subscribe(topic)
    cl.loop_forever()


run()
