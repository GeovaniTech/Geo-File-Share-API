import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from gunicorn.app.base import BaseApplication

from routes.Client import clients_bp
from routes.Files import files_bp
from routes.Common import commons_bp
from routes.Plan import plans_bp

app = Flask(__name__)
app.register_blueprint(files_bp, url_prefix="/fileshare/")
app.register_blueprint(commons_bp, url_prefix="/fileshare/")
app.register_blueprint(clients_bp, url_prefix="/fileshare/")
app.register_blueprint(plans_bp, url_prefix="/fileshare/")


@app.before_request
def verify_api_key():
    api_key = request.headers.get('Api-Key')

    if api_key is None or os.getenv("API_KEY") != api_key:
        return jsonify(message = "API key is invalid"), 401

    return None


if __name__ == '__main__':
    load_dotenv()

    project_root = os.path.abspath(os.path.dirname(__file__))

    if project_root == '/projects/Geo-File-Share-API':
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

        ssl_context = (
            '/certs/certificate.crt',
            '/certs/key.key'
        )

        options = {
            'bind': '0.0.0.0:8001',
            'workers': 4,
            'certfile': ssl_context[0],
            'keyfile': ssl_context[1],
        }

        StandaloneApplication(app, options).run()
    else:
        app.run(host='0.0.0.0', port="5000", debug=True)
