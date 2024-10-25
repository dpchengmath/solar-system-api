from flask import Blueprint, abort, make_response, Response, request
from app.models.planet import Planet
from ..db import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    planets = db.session.scalars(query)

    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    
    description_query = request.args.get("description")
    if description_query:
        planets = Planet.query.filter_by(description=description_query)

    diameter_query = request.args.get("diameter")
    if diameter_query:
        planets = Planet.query.filter_by(diameter=diameter_query)

    else:
        planets = Planet.query.all()

    planet_response = []

    for planet in planets:
        planet_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "diameter": planet.diameter
            }
        )
    return planet_response


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    diameter = request_body["diameter"]

    new_planet = Planet(name=name, description=description, diameter=diameter)
    db.session.add(new_planet)
    db.session.commit()

    response = {

        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "diameter": new_planet.diameter
    }
    return response, 201


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id) 

    return {

        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "diameter": planet.diameter
    }


@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))
    
    return planet 