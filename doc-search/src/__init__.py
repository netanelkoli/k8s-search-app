import sys, os, time
from index import Index
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

SLEEP_TIME=60
app = Flask(__name__)
index = Index.new(sys.argv[1])
metrics = PrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def search():
    q = request.args.get('q', default="")
    print(q, type(q))
    return dict(results=list(index.search(str(q))))

@app.route('/health')
def health():
    return "healthy"

if __name__ == '__main__':
    test_load = os.environ.get('TEST_LOAD', default='false')
    print(f"Simulating a heavy load on start-up: {test_load}")
    if test_load == 'true':
        time.sleep(SLEEP_TIME)
    app.run(port=8080, host="0.0.0.0")
