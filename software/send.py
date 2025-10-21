import paho.mqtt.client as mqtt
import time

# MQTT Configuration (emqx public broker))
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
# Topic to publish or subscribe to
MQTT_TOPIC = "forgescam/security"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_start()

messege = "This is a test message for MQTT publishing."
client.publish(MQTT_TOPIC, messege)

# Allow a short time to make sure messege is sent before ending script
time.sleep(2)

# Stops background MQTT thread from earlier
client.loop_stop()
# Disconnects from the broker
client.disconnect()