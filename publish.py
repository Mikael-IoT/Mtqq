import paho.mqtt.client as paho
import random
import time

CLIENT_ID = f'kyh-mqtt-{random.randint(0, 1000)}'
USERNAME = 'kyh_mikael'
PASSWORD = 'passwords'
BROKER = 's11df6c1.eu-central-1.emqx.cloud'
PORT = 15914


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to MQTT Broker')
    else:
        print(f'Failed to connect to Broker. Error code {rc}')


def connect_mqtt():
    # Create a MQTT client object
    # Every client has an id.
    client = paho.Client(CLIENT_ID)
    # Set a username and a password to connect to broker
    client.username_pw_set(USERNAME, PASSWORD)

    # When connection response is received
    # We run the on_connect function
    client.on_connect = on_connect

    # Connect to broker
    client.connect(BROKER, PORT)

    return client


def main():
    client = connect_mqtt()
    # start the paho loop that will
    # spawn a new thread and send and receive messages
    client.loop_start()
    sub_topic = input('Publish to what sub-topic?')

    while True:
        # Get current temperature
        temp = random.uniform(15.0, 25.0)
        # Publish to the topic temperature/room1 with temp
        client.publish(f'temperature/{sub_topic}', str(temp))
        # Interval to publish messages
        time.sleep(1)

    client.loop_stop()


if __name__ == '__main__':
    main()
