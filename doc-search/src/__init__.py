import sys, os, time
from index import Index
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

SLEEP_TIME=60
app = Flask(__name__)
index = Index.new(sys.argv[1])
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/')
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
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
