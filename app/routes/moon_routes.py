from flask import Blueprint, request, make_response, abort
from app.models.moon import Moon
from .route_utilities import validate_model
from app.models.planet import Planet
from ..db import db

bp = Blueprint("moon_bp", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    return 
  


@bp.get("")
def read_all_moons():
    return


@bp.post("/<moon_id>/planets")
def create_planet_with_moon_id(moon_id):
    moon = validate_model(moon, moon_id)


    request_body = request.get_json()
    request_body["moon_id"] = moon.id

