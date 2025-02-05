import json
from collections import defaultdict
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Kafka Configuration
TOPIC = "project_json"
KAFKA_SERVER = "localhost:9092"

# Data Storage
message_counts = defaultdict(int)  # Store total message counts per category

# Consumer Setup
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    """Function to consume messages from Kafka and update message counts."""
    print("Waiting for messages...")
    for message in consumer:
        data = message.value
        category = data.get("category", "other")
        
        # Increment the count for this category
        message_counts[category] += 1

        print(f"Updated message counts: {message_counts}")

def animate(i):
    """Function to update the real-time visualization."""
    plt.cla()
    categories = list(message_counts.keys())
    counts = list(message_counts.values())
    
    # Define unique colors for categories
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'pink'][:len(categories)]
    
    plt.bar(categories, counts, color=colors)
    plt.xlabel("Categories")
    plt.ylabel("Total Messages")
    plt.title("Real-Time Total Messages by Category - David Rodriguez")
    plt.xticks(rotation=45)

# Main
if __name__ == "__main__":
    # Start Kafka consumer in the background
    import threading
    threading.Thread(target=consume_messages, daemon=True).start()

    # Start Matplotlib animation
    fig = plt.figure()
    ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
    plt.show()

