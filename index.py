from flask import Flask, jsonify, request, send_from_directory
from modules.generate import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return send_from_directory('files', 'index.html')

@app.route("/public/<path:path>", methods=["GET"])
def public(path):
    return send_from_directory('public', path)

@app.route("/length/", methods=["GET"])
def length():
    length = get_length(request)
    return jsonify(length=length)

@app.route("/generate/", methods=["GET"])
def generate():
    length = get_length(request)
    if length > 10000:
        return jsonify(password="Error", length=length, success=False, error="Requested length is too long, max length is " + max_length + " generated chars"), 400

    password = generate_password(length)
    password = salt_password(request, password)
    password = add_pepper(request, password)
    return jsonify(password=password, length=len(password), success=True, error="None")

if __name__ == "__main__":
    app.run(port=3000)