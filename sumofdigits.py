from flask import Flask

app = Flask(__name__)


@app.route('/sum/<int:n>')
def int_input(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)
    return 'Sum is:  %d'%sum


if __name__ == '__main__':
    app.debug = True
    app.run()


