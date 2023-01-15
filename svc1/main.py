from flask import Flask
#from gunicorn.app.wsgiapp import 
import gunicorn.app.base
import logging

logging.basicConfig(level=logging.INFO)
from src import f1
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == "__main__":
    logging.info("Hola from py")
    f1.F1()
    logging.info(f"3 + 4 = {f1.Suma(3,4)}")
    app = Flask(__name__)
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8080'),
        'workers': 1,
    }
    StandaloneApplication(app, options).run()