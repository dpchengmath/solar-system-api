import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
from app.models.planet import Planet
import os


load_dotenv()


@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    with app.app_context():
    
        mercury_planet = Planet(name="Mercury",
                        description="Hottest planet",
                        diameter=4879)
        
        neptune_planet = Planet(name="Neptune",
                            description="Giant and icy planet",
                            diameter=49244)

        db.session.add_all([mercury_planet, neptune_planet])
        db.session.commit()    