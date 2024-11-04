from flask import Blueprint, abort, make_response, Response, request
from app.models.planet import Planet
from sqlalchemy import desc
from .route_utilities import validate_model
from ..db import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)

    name_query = request.args.get("name")
    if name_query:
        query = query.where(Planet.name.ilike(f"%{name_query}%"))
    
    description_query = request.args.get("description")
    if description_query:
        query = query.where(Planet.description.ilike(f"%{description_query}%"))

    diameter_query = request.args.get("diameter")
    if diameter_query:
        query = query.where(Planet.diameter.ilike(f"%{diameter_query}%"))

    query = query.order_by(desc(Planet.diameter))
    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]

    return planets_response


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id) 

    return planet.to_dict()


@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")