from flask import Flask
import redis
import logging
import os

app = Flask(__name__)

# configure logger
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)


redis_host = os.environ.get('REDIS_HOST', 'redis-server')
redis_port = 6379

redis_client = redis.Redis(host=redis_host, port=redis_port)
visits = 0
redis_client.set('visits', 0)


@app.route('/')
def home():
    val = int(redis_client.get('visits'))
    app.logger.info(val)
    redis_client.set('visits', int(val) + 1)

    return f"Total Number of Visits: {val}"


if __name__ == '__main__':
    app.run()

