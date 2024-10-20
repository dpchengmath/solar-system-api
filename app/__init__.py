from flask import Flask
from .routes.planet_routes import planets_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    app.register_blueprint(planets_bp)

    return app