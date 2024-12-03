from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/calculate" method="post">
            Number 1: <input type="text" name="num1"><br>
            Number 2: <input type="text" name="num2"><br>
            Operation (+, -, *, /): <input type="text" name="operation"><br>
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Invalid operation. Use +, -, *, or /."
        return f"Result: {result}"
    except ValueError:
        return "Invalid input. Please enter numeric values."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
