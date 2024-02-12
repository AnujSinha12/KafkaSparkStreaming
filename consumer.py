from kafka import KafkaConsumer
import json

# registered_user: Topic name from where to consume data
# auto_offset_reset: get message from earliest or latest
# group_id: consumer group belong to particular group id

KAFKA_SINK_TOPIC = 'sink'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'


if __name__ == '__main__':
    consumer = KafkaConsumer(
        KAFKA_SINK_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        group_id='consumer-group-1'
    )

    print('Consumer Started')

    for msg in consumer:
        print(f'Registered User = {json.loads(msg.value)}')


