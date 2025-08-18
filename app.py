import time

import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retrives = 5
    while True:
        try:
            #cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retirves == 0:
                raise exc
            retrives -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello Maddy! I have been seen {} times.\n'.format(count)