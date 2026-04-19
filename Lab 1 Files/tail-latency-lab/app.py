from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    # Most requests are fast, a few are slow
    delay = random.choice(
        [random.uniform(0.01, 0.05)] * 90 +
        [random.uniform(0.2, 0.5)] * 10
    )
    time.sleep(delay)
    return jsonify({"delay_seconds": delay})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)