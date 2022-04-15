from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello world!'


@app.route('/<operator>/<num1>/<num2>')
def calculate(operator, num1, num2):

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return 'Not numbers'

    match operator:
        case 'add':
            return str(num1 + num2)
        case 'sub':
            return str(num1 - num2)
        case 'mul':
            return str(num1 * num2)
        case 'div':
            return str(num1 / num2)
        case _:
            return 'Invalid operation'


if __name__ == '__main__':
    app.run()
