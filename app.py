from flask import Flask
from waitress import serve
from loguru import logger


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! (again ;)'


if __name__ == '__main__':
    port = 80
    logger.info(f"Starting app on port {port}")
    serve(app, port=port)
