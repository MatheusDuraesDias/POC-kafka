from confluent_kafka import Consumer, KafkaError

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'M_and_M', 'auto.offset.reset': 'earliest'})
c.subscribe(['temps'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()