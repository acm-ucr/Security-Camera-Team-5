import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "forgescam/security"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)   # Subscribe to the topic after connection is established

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")  # Decode and print the message payload

client = mqtt.Client()
client.on_connect = on_connect      # Set callback for when connection is made
client.on_message = on_message      # Set callback for when a message arrives

client.connect(MQTT_BROKER, MQTT_PORT, 60)  # Connect to the broker

client.loop_forever()               # Start the network loop and block forever to keep listening
