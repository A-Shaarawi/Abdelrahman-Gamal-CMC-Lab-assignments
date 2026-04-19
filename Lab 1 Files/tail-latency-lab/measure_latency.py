import requests
import time
import matplotlib.pyplot as plt

URL = "http://127.0.0.1:5000/"
NUM_REQUESTS = 200

latencies = []

for _ in range(NUM_REQUESTS):
    start = time.time()
    requests.get(URL)
    end = time.time()
    latencies.append((end - start) * 1000)  # ms

print(f"Min latency: {min(latencies):.2f} ms")
print(f"Max latency: {max(latencies):.2f} ms")
print(f"Average latency: {sum(latencies)/len(latencies):.2f} ms")

plt.hist(latencies, bins=30, edgecolor='black')
plt.title("Response Time Histogram")
plt.xlabel("Latency (ms)")
plt.ylabel("Frequency")
plt.savefig("latency_histogram.png")
plt.show()