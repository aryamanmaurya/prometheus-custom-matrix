from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Create a Counter to track the number of requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests to the app')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()  # Increment counter
    return 'Hello, World!'

# Expose metrics to Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

