from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/calculate" method="post">
            Grades (comma-separated): <input type="text" name="grades"><br>
            <input type="submit" value="Calculate CGPA">
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        grades = list(map(float, request.form['grades'].split(',')))
        if not grades:
            return "Please enter at least one grade."
        cgpa = sum(grades) / len(grades)
        return f"CGPA: {cgpa:.2f}"
    except ValueError:
        return "Invalid input. Please enter numeric grades separated by commas."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
