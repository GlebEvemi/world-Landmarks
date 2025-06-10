from app import app
from app.middlewares.authorize import authorized
from models.User import User
from flask import jsonify, send_from_directory
from flask import request
from werkzeug.utils import secure_filename
import os
from service.photo import create_photo, delete_photo, get_landmark_photos


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')


@app.route("/landmark/<int:landmark_id>/photo", methods=["POST"])
@authorized
def upload_photo(landmark_id: int, user: User):
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if not file.filename:
        return jsonify({"error": "No selected file"}), 400
    filename = secure_filename(file.filename)
    create_photo(
        landmark_id=landmark_id, 
        user=user,
        filename=filename,
        photo=file,
    )
    return jsonify({
        "filename": filename,
        "message": "Photo uploaded",
    }), 200


@app.route("/landmark/<int:landmark_id>/photo", methods=["DELETE"])
@authorized
def d_photo(landmark_id: int, user: User):
    try:
        photos = delete_photo(l)

        return jsonify(list(p.to_dict(request.host_url) for p in photos)), 200 
    except:
        return jsonify({
            "error": "Landmark not found."
        }), 404


@app.route("/landmark/<int:landmark_id>/photo", methods=["GET"])
def list_photos(landmark_id: int):
    try:
        photos = get_landmark_photos(landmark_id)

        return jsonify(list(p.to_dict(request.host_url) for p in photos)), 200 
    except:
        return jsonify({
            "error": "Landmark not found."
        }), 404


@app.route("/uploads/<filename>")
def get_photo(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
