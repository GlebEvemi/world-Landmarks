from sqlalchemy import and_
from werkzeug.datastructures import FileStorage
from models.Landmark import Landmark
from models.Photo import Photo
from models.Rating import Rating
from models.User import User
from app import db


def create_rating(user: User, landmark_id: int, mark: int):
    rating = Rating(mark, user.id, landmark_id)
    db.session.add(rating)
    db.session.commit()


def delete_rating(user: User, rating_id: int):
    ...


def update_rating(user: User, rating_id: int, mark: int):
    ...


def get_average_rating(landmark_id: int):
    ...
