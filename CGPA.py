from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for better user interface
html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGPA Calculator</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 20px; }
      h1 { color: #4CAF50; }
      label, input { margin-top: 10px; display: block; }
      input[type="text"] { padding: 8px; width: 300px; }
      input[type="submit"] { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
      input[type="submit"]:hover { background-color: #45a049; }
      .result { font-size: 18px; font-weight: bold; color: #333; margin-top: 20px; }
    </style>
  </head>
  <body>
    <h1>CGPA Calculator</h1>
    <p>Enter your grades (comma-separated) below to calculate your CGPA.</p>
    <form action="/calculate" method="post">
      <label for="grades">Grades (e.g., 8.5, 9.0, 7.5):</label>
      <input type="text" id="grades" name="grades" required placeholder="Enter grades separated by commas">
      <input type="submit" value="Calculate CGPA">
    </form>
    {% if cgpa %}
    <div class="result">Your CGPA is: {{ cgpa }}</div>
    {% endif %}
  </body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get grades from the user input and calculate CGPA
        grades = list(map(float, request.form['grades'].split(',')))
        if not grades:
            return render_template_string(html_template, cgpa="Please enter at least one grade.")
        cgpa = sum(grades) / len(grades)
        return render_template_string(html_template, cgpa=f"{cgpa:.2f}")
    except ValueError:
        return render_template_string(html_template, cgpa="Invalid input. Please enter numeric grades separated by commas.")

if __name__ == '__main__':
    app.run(debug=True)
