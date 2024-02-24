from flask import Blueprint

results = Blueprint('results', __name__)

@results.route('/flights')
def volver():
    return "<p>Login</p>"