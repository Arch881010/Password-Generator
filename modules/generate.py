import random
import string
from flask import jsonify, request


default_salt = ""
default_pepper = ""
max_length = 10000


def get_length(req):
    length = req.args.get("length", default=10, type=int)
    return length

def too_long(length):
    if length > max_length:
        return jsonify(error="Password too long"), 400
    return jsonify(success="Password length is fine"), 200


def generate_password(length):
    charset = string.ascii_letters + string.digits
    password = "".join(random.choice(charset) for _ in range(length))
    return password


def salt_password(request, password):
    salt = request.args.get("salt", default=default_salt, type=str)
    return salt + password


def add_pepper(request, password):
    pepper = request.args.get("pepper", default=default_pepper, type=str)
    return password + pepper

