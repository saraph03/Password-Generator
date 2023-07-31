from flask import Flask, jsonify
from psswdgen import password_generator
app = Flask(__name__)

@app.route("/generate-password")
def generate_password():
    password = password_generator()
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)