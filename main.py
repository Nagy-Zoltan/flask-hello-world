from flask import Flask


app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello world!'


@app.route('<operator>:string/<num1>:int/<num2>:int')
def calculate(operator, num1, num2):
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
