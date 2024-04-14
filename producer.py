from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging as log
from configobj import ConfigObj

config = ConfigObj('config.env')

server = config['SERVER']
port = config['PORT']
topic_name = config['TOPIC_NAME']
msg = "Hello There"

producer = KafkaProducer(bootstrap_servers=[server+":"+port])

future = producer.send(topic_name, msg.encode('utf-8'))

record_metadata = ""

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception(0)
    pass
# Successful result returns assigned partition and offset
print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)
