from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '1st Page: Prabhu'


@app.route('/prabhu')
def second_page():
    return '2nd page: Welcome'


if __name__ == '__main__':
    app.debug = True
    app.run()


