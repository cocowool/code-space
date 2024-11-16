from kafka import KafkaProducer;
import json

# producer = KafkaProducer(
#     value_serializer = lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=['127.0.0.1:9092']
# )

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

msg_dict = {
    "tc" : "A00001",
    "appid" : 401,
    "amt" : 1000,
    "st" : "2024-11-15"
}

msg = "hello world".encode('utf-8')

# producer.send("test_flink_input", msg_dict)
producer.send("test_flink_input", msg)
producer.close()