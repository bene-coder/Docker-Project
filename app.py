from flask import Flask, render_template_string, request

# Create the Flask app
app = Flask(__name__)

# Define a simple HTML template for the form
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Benedictus' Simple Flask App</title>
</head>
<body>
    <h1>Benedictus' Simple Flask App</h1>
    <form action="/" method="post">
        <label for="name">Enter your name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <input type="submit" value="Submit">
    </form>
    {% if name %}
        <p>Hello, {{ name }}!</p>
    {% endif %}
</body>
</html>
"""

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template_string(template, name=name)
    return render_template_string(template)

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
