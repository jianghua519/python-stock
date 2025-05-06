import requests
import json
from kafka import KafkaProducer
import schedule
import time

# Kafka 配置
KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "stock_data"

# API 配置
API_URL = "https://jsonplaceholder.cypress.io/todos/1"

# Kafka 生产者
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# 数据抓取函数
def fetch_stock_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # 发送数据到 Kafka
        producer.send(KAFKA_TOPIC, data)
        print(f"数据已发送至 Kafka: {data}")

    except requests.exceptions.RequestException as e:
        print(f"抓取数据失败: {e}")

# 定时任务，每 10 分钟抓取一次数据
schedule.every(10).minutes.do(fetch_stock_data)

# 运行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)
