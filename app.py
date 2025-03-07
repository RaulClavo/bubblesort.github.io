from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/generate')
def generate_number():
    return str(random.randint(100000, 999999))

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
