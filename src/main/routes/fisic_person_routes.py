from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.fisic_person_creator_composer import fisic_person_creator_composer
from src.main.composer.fisic_person_finder_composer import fisic_person_finder_composer

from src.errors.error_handler import handle_errors

fisic_person_route_bp = Blueprint("fisic_person_routes", __name__)

@fisic_person_route_bp.route("/fisic_person", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = fisic_person_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@fisic_person_route_bp.route("/fisic_person/<person_id>", methods=["GET"])
def find_person(person_id):
    try:
        http_request = HttpRequest(param={"person_id": person_id})
        view = fisic_person_finder_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
