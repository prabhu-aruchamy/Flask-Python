from flask import Flask

app = Flask(__name__)

#http://127.0.0.1:5000/tlt/prabhu
#http://127.0.0.1:5000/prabhu



@app.route('/<name>')
def hello_name(name):
    return 'Hello %s!'%name


@app.route('/tlt/<inpt>')
def hello_n(inpt):
    return 'Second Page input:  %s!'%inpt


@app.route('/intinput/<int:intinp>')
def int_input(intinp):
    return 'Integer input:  %d'%intinp


if __name__ == '__main__':
    app.debug = True
    app.run()


