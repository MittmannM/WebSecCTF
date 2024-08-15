from paho.mqtt import client as mqtt_client


broker = "10.157.150.7"
port = 1883
topic = "#"


def connect_mqtt() -> mqtt_client:
    cl = mqtt_client.Client()
    cl.on_connect = lambda client, userdata, flags, rc: (
        print(f"Connected to MQTT Broker! Subscribed to topic '{topic}'!" if rc == 0 else f"Failed to connect, RC {rc}"))
    cl.username_pw_set(username="roger", password="password")
    cl.connect(broker, port)
    return cl


def subscribe(cl: mqtt_client):
    cl.subscribe(topic)
    cl.on_message = lambda client, userdata, msg: (
        print(f"{msg.topic}:{' ' * (40 - len(msg.topic))}{msg.payload.decode()}"))
    return


def run():
    cl = connect_mqtt()
    subscribe(cl)
    cl.loop_forever()


run()
