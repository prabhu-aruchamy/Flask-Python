from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<name>')
def hello_guest(name):
    return 'Hello Guest: %s!'%name


@app.route('/user/<namee>')
def hello_user(namee):
    if namee == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', name=namee))


if __name__ == '__main__':
    app.debug = True
    app.run()


