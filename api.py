import os

from dotenv import load_dotenv
from flask import Flask
from gunicorn.app.base import BaseApplication

from routes.Client import clients_bp
from routes.Files import files_bp
from routes.Common import commons_bp

app = Flask(__name__)
app.register_blueprint(files_bp, url_prefix="/fileshare/")
app.register_blueprint(commons_bp, url_prefix="/fileshare/")
app.register_blueprint(clients_bp, url_prefix="/fileshare/")

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
