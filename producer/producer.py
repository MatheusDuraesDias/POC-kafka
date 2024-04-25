from confluent_kafka import Producer
import json

p = Producer({'bootstrap.servers': 'localhost:9092'})

for i in range(26):

    loc = input('digite o estado: \n')
    temp = input('digite a temperatura: \n')
    region = input('digite a região(ex: Sul, Centro-Oeste): \n')
    stop = input('continuar? (s/n)')

    json_event = {
        'clime': {
            'location': loc,
            'temperature': temp
        }
    }

    json_str = json.dumps(json_event)

    p.produce('temps', value=json_str, key=region)
    p.flush()
    if stop != 's':
        break