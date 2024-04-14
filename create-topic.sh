# import config
source config.env

# create topic
kafka-topics --delete --bootstrap-server $"SERVER":$"PORT" --topic $"TOPIC_NAME"
kafka-topics --create --bootstrap-server $"SERVER":$"PORT" --replication-factor $"REPLICATION_FACTOR" --partitions $"PARTITION_COUNT" --topic $"TOPIC_NAME"