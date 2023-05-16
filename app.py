from flask import Flask
from waitress import serve
from loguru import logger


app = Flask(__name__)


@app.route('/')
def hello_world_root():
    return 'Hello World! (from root)'


@app.route('/e1')
def hello_world_1():
    return 'Hello World! (from endpoint 1)'


@app.route('/e2')
def hello_world_2():
    return 'Hello World! (from endpoint 2)'


if __name__ == '__main__':
    port = 80
    logger.info(f"Starting app on port {port}")
    serve(app, port=port)
