from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from gunicorn.app.base import BaseApplication

import os

app = Flask(__name__)

@app.before_request
def verify_api_key():
    api_key = request.headers.get('Api-Key')

    if api_key is None or os.getenv("API_KEY") != api_key:
        return jsonify(message = "API key is invalid"), 401

    return None


@app.route("/fileshare/test", methods=["GET", "POST"])
def test_endpoint():
    return make_response(
        jsonify(
            message = "Hello, world!"
        )
    ), 200


if __name__ == '__main__':
    load_dotenv()

    project_root = os.path.abspath(os.path.dirname(__file__))

    if project_root == '/projects/Geo-File-Share-Api':
        class StandaloneApplication(BaseApplication):
            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super(StandaloneApplication, self).__init__()

            def load_config(self):
                config = {key: value for key, value in self.options.items() if
                          key in self.cfg.settings and value is not None}
                for key, value in config.items():
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        options = {
            'bind': '0.0.0.0:8001',
            'workers': 4
        }

        StandaloneApplication(app, options).run()
    else:
        app.run(host='0.0.0.0', port="5000", debug=True)
