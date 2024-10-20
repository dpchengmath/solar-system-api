from flask import Blueprint, abort, make_response, request
from app.models.planet import planets
# from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
        )
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id) 

    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
            }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))

# @planets_bp.post("")
# def create_planet():
#     request_body = request.get_json()
#     title = request_body["title"]
#     description = request_body["description"]

#     new_book = Planet(title=title, description=description)
#     db.session.add(new_planet)
#     db.session.commit()

#     response = {
#         "id": new_planet.id,
#         "title": new_planet.name,
#         "description": new_planet.description,
#     }
#     return response, 201
