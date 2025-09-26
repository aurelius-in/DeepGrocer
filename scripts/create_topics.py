import json, os, sys
from kafka.admin import KafkaAdminClient, NewTopic


def main():
    broker = os.getenv("KAFKA_BROKER", "localhost:9092")
    path = sys.argv[1] if len(sys.argv) > 1 else "config/kafka/topics.json"
    with open(path, "r") as f:
        spec = json.load(f)
    admin = KafkaAdminClient(bootstrap_servers=broker, client_id="deepgrocer-admin")
    topics = [
        NewTopic(name=t["name"], num_partitions=t.get("partitions", 1), replication_factor=t.get("replication_factor", 1))
        for t in spec.get("topics", [])
    ]
    try:
        admin.create_topics(new_topics=topics, validate_only=False)
        print(f"Created {len(topics)} topics")
    except Exception as e:
        print(f"Topic creation skipped or failed: {e}")


if __name__ == "__main__":
    main()

