from flask import Flask, request


app = Flask(__name__)


@app.before_request
def filter_non_python():
    user_agent = request.headers['User-Agent']
    if not user_agent.startswith('python-requests'):
        return 'Only python requests is allowed', 403


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
