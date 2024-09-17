import pika
import random
import string
import threading
from time import sleep

def sender_device(name, host, queue_name, creds, num_messages):
    creden = pika.PlainCredentials(*creds)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=creden))
    channel = connection.channel()

    try:
        channel.queue_declare(queue=queue_name)
    except Exception as e:
        print(f"Queue declaration failed: {e}")

    try:
        for _ in range(num_messages):
            data = random.choice(string.ascii_letters)        
            channel.basic_publish(exchange="", routing_key=queue_name, body=data)
            print(f"[x] Sent by {name}: {data}")
        
    finally:
        connection.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="RabbitMQ Sender Script")
    parser.add_argument('--host', type=str, default="localhost", help="RabbitMQ server host")
    parser.add_argument('--queue', type=str, default="hello", help="Queue name")
    parser.add_argument('--username', type=str, default="test", help="RabbitMQ username")
    parser.add_argument('--password', type=str, default="test", help="RabbitMQ password")
    parser.add_argument('--messages', type=int, default=10000, help="Number of messages to send per thread")
    parser.add_argument('--threads', type=int, default=8, help="Number of threads to use")
    
    args = parser.parse_args()
    
    creds = (args.username, args.password)
    
    for i in range(args.threads):
        name = f"Thread-{i}"
        thread = threading.Thread(target=sender_device, args=(name, args.host, args.queue, creds, args.messages))
        thread.start()
