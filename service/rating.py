from flask.app import cli
from sqlalchemy import and_
from werkzeug.datastructures import FileStorage
from models.Landmark import Landmark
from models.Photo import Photo
from models.Rating import Rating
from models.User import User
from app import db
from sqlalchemy import func
from numpy import clip

from service.landmark import get_landmark_by_id

def create_rating(user: User, landmark_id: int, mark: int, comment: str):
    mark = clip(mark, 1, 5)
    rating = Rating(mark, user.id, landmark_id, comment)
    db.session.add(rating)
    db.session.commit()

    return rating


def delete_rating(user: User, rating_id: int):
    rating: Rating = Rating.query.filter(and_(
        Rating.id == rating_id,
        Rating.user_id == user.id
    )).first()

    if not rating:
        raise ValueError("Rating not found")

    db.session.delete(rating)
    db.session.commit()


def update_rating(user: User, rating_id: int, mark: int, comment: str):
    mark = clip(mark, 1, 5)

    rating: Rating = Rating.query.filter(and_(
        Rating.id == rating_id,
        Rating.user_id == user.id
    )).first()
    
    if not rating:
        raise ValueError("Rating not found")
    
    rating.rating = mark
    rating.comment = comment

    db.session.commit()


def get_average_rating(landmark_id: int):
    result = db.session.query(func.avg(Rating.rating))\
        .filter(Rating.landmark_id == landmark_id)\
        .scalar()
    lm = get_landmark_by_id(landmark_id)

    if not lm:
        raise ValueError("Landmark not found")
    avg_rating = float(result) if result is not None else 0.0 
    lm.average_rating = avg_rating
    
    db.session.commit()

    return avg_rating

def list_ratings(landmark_id: int) -> list[Rating]:
    ratings = Rating.query.filter_by(landmark_id=landmark_id).all()

    return ratings
