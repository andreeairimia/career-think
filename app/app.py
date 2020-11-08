from flask import Flask
from views import bp as frontend_bp
from api import bp as network_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'

if __name__ == "__main__":
    app.register_blueprint(frontend_bp)
    app.register_blueprint(network_bp)
    app.run(debug=True)
