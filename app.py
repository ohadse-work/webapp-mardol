from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for a form submission
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)