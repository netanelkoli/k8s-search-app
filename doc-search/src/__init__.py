import sys, os, time
from index import Index
from bottle import route, run, template, request

SLEEP_TIME=60

if __name__ == '__main__':
    index = Index.new(sys.argv[1])
    test_load = os.environ.get('TEST_LOAD', default='false')
    print(f"Simulating a heavy load on start-up: {test_load}")

    if test_load == 'true':
        time.sleep(SLEEP_TIME)

    @route('/')
    def search():
        q = request.query.q
        print(q, type(q))
        return dict(results=list(index.search(str(q))))


    @route('/health')
    def health():
        return "healthy"

    run(host="0.0.0.0")
