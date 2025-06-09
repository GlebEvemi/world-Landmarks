from app import app
from app.middlewares.authorize import authorized
from models.User import User
from flask import jsonify, send_from_directory
from flask import request
from werkzeug.utils import secure_filename
import os
from service.rating import create_rating, delete_rating, get_average_rating, list_ratings, ratin, update_rating
from service.photo import create_photo, get_landmark_photos


@app.route("/landmark/<int:id>/rating")
def get_rating(id: int):
    try:
        rating = get_average_rating(id)

        ratings = list_ratings(id) 

        return jsonify({
            "comments": list(r.to_dict for r in ratings),
            "averageRating": rating
        }), 200
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        }), 400


@app.route("/landmark/<int:id>/rating", methods=["POST"])
@authorized
def cr_rating(id: int, user: User):
    data = request.get_json()
    try:
        mark = data.get("mark")
        comment = data.get("comment")

        rating = create_rating(user, id, mark, comment)
        return jsonify(rating.to_dict()), 200 
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        }), 400


@app.route("/rating/<int:id>", methods=["PUT"])
@authorized
def cr_rating(id: int, user: User):
    data = request.get_json()
    try:
        mark = data.get("mark")
        comment = data.get("comment")

        update_rating(user, id, mark, comment)
        return jsonify({
            "message": "Successfully updated the rating"
        }), 200 
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        }), 400


@app.route("/rating/<int:id>", methods=["DELETE"])
@authorized
def d_rating(id: int, user: User):
    try:
        delete_rating(user, id) 
        return jsonify({
            "message": "Successfully deleted the rating"
        }), 200 
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        }), 400
