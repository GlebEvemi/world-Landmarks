from app import app
from app.middlewares.authorize import authorized
from models.User import User
from models.Landmark import Landmark
from service.landmark import create_landmark, delete_landmark
from flask import jsonify
from flask import request


@app.route("/landmark", methods=["POST"])
@authorized
def cr_landmark(user: User):
    data = request.get_json()
    try:
        with app.app_context():
            name = data.get("name")
            description = data.get("description")
            location = data.get("location")
            country = data.get("country")
            landmark: Landmark = create_landmark(
                user=user,
                name=name,
                description=description,
                location=location,
                country=country
            )

            return jsonify(landmark.to_dict()), 200
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        }), 400


@app.route("/landmark/<int:id>", methods=["PUT"])
@authorized
def u_landmark(id: int, user: User):
    return "Unimplemented", 501


@app.route("/landmark/<int:id>", methods=["DELETE"])
@authorized
def d_landmark(id: int, user: User):
    try:
        with app.app_context():
            delete_landmark(user, id)
            return jsonify({
                "message": "Successfully deleted the landmark."
            }), 200
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        }), 400
