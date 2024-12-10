import time
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Create a registry to store metrics
registry = CollectorRegistry()

# Create a metric (e.g., duration of a task)
task_duration = Gauge('task_duration_seconds', 'Time taken by task', registry=registry)

def simulate_task():
    """Simulate a serverless task."""
    start_time = time.time()
    print("Task started.")
    time.sleep(2)  # Simulate task running for 2 seconds
    duration = time.time() - start_time
    print(f"Task completed in {duration} seconds.")
    return duration

def push_metrics():
    """Push metrics to Pushgateway."""
    duration = simulate_task()
    task_duration.set(duration)

    # Push metrics to Pushgateway
    push_to_gateway('localhost:9091', job='example_serverless_task', registry=registry)
    print("Metrics pushed to Pushgateway.")

if __name__ == "__main__":
    push_metrics()
