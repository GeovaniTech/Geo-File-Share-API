from api import app
from flask import request, jsonify

import os

@app.before_request
def verify_api_key():
    api_key = request.headers.get('Api-Key')

    if api_key is None or os.getenv("API_KEY") != api_key:
        return jsonify(message = "API key is invalid"), 401

    return None