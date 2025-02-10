# app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sensitive-data')
def sensitive_data():
    # Simulating sensitive data
    sensitive_info = {
        "username": "admin",
        "password": "supersecretpassword123",
        "api_key": "12345-abcde-67890",
        "db_password": "dbsupersecretpass"
    }
    return jsonify(sensitive_info)

if __name__ == "__main__":
    app.run(debug=True)
