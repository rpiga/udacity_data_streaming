from kafka import KafkaConsumer
import json
import time


if __name__ == "__main__":
    topic = 'com.udacity.project.spark'
    
    bootstrap_servers = 'localhost:9092'
    
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    for msg in consumer:
        m = msg.value
        print(f"crime: {m['original_crime_type_name']}, disposition: {m['disposition']}")