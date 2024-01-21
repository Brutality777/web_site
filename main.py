import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

@app.route('/by_name/<name>')
def index(name):
    return jsonify({'name': name,
                    'email': name+'@outlook.com'})

app.run()