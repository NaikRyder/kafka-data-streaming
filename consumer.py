from kafka import KafkaConsumer
from configobj import ConfigObj

config = ConfigObj('config.env')

server = config['SERVER']
port = config['PORT']
topic_name = config['TOPIC_NAME']

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic_name, bootstrap_servers=[server + ":" + port])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("topic=%s\tpartition=%d\toffset=%d\tmsg=%s" % (message.topic,
                                 message.partition,
                                 message.offset,
                                 message.value))
