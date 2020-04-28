import os
from flask import Flask

app = Flask(__name_)


@app.route('/')
def hello():
    return 'Hello World....again'


if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            port=int(os.environ.get('5000')),
            debug=True)  