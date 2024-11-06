from flask import Blueprint, abort, make_response, Response, request
from app.models.planet import Planet
from sqlalchemy import desc
from .route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body)


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