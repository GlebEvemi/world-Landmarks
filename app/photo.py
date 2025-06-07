from app import app
from app.middlewares.authorize import authorized
from models.User import User
from models.Landmark import Landmark
from service import landmark
from service.landmark import create_landmark, delete_landmark, get_landmark_by_id, list_landmarks, update_landmark
from flask import jsonify
from flask import request


@app.route("/landmark/<int:landmark_id>/photo", methods=["POST"])
@authorized
def upload_photo(landmark_id: int, user: User):
    return "Unimplemented", 500


@app.route("/landmark/<int:landmark_id>/photo", methods=["POST"])
@authorized
def delete_photo(landmark_id: int, user: User):
    return "Unimplemented", 500


@app.route("/landmark/<int:landmark_id>/photo", methods=["POST"])
def list_photos(landmark_id: int):
    return "Unimplemented", 500
