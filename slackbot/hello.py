import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('hello', __name__, url_prefix='/')

@bp.route('/bonjour', methods=['GET'])
def bonjour():
    data = {
        "greeting": "bonjour"
    }
    return jsonify(data)

@bp.route('/hola', methods=['GET'])
def hola():
    data = {
        "greeting": "hola"
    }
    return jsonify(data)