from kafka import KafkaProducer
from data import get_registered_user
import json, time


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


# def get_partition(key, all, available):
# """ Set to partition 0 only """
#     return 0


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=json_serializer)


if __name__ == '__main__':
    # running infinitely with delay to create streaming data like condition
    print("Producer Started")
    while True:
        registered_user = get_registered_user()
        print(registered_user)
        # Send the data to kafka server
        producer.send('registered_user', registered_user)
        time.sleep(4)
