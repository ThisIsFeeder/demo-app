import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello from demo-app {os.environ.get('APP_VERSION', '0.0.0')}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
