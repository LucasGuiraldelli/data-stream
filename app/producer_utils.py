from kafka import KafkaProducer
import requests
import json

def buscar_e_enviar():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    data = response.json()

    payload = {
        'id': data['id'],
        'titulo': data['title'],
        'concluido': data['completed']
    }

    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send('dados_api', payload)
    producer.flush()
    print("Mensagem enviada ao Kafka:", payload)
