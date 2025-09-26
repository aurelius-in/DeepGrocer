import asyncio, json, os
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

BROKER = os.getenv("KAFKA_BROKER","kafka:9092")

async def get_producer():
    prod = AIOKafkaProducer(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode())
    await prod.start()
    return prod

def consumer(topic: str, group_id: str):
    return AIOKafkaConsumer(
        topic,
        bootstrap_servers=BROKER,
        group_id=group_id,
        value_deserializer=lambda m: json.loads(m.decode()),
        enable_auto_commit=True
    )
