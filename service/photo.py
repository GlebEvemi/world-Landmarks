import os
from sqlalchemy import and_
from werkzeug.datastructures import FileStorage
from models.Landmark import Landmark
from models.Photo import Photo
from models.User import User
from app import db
from service.landmark import get_landmark_by_id


def create_photo(
    landmark_id: int, 
    user: User, 
    filename: str,
    photo: FileStorage,
):
    if not user:
        raise ValueError("Unauthorized")

    lm: Landmark = Landmark.query.filter(and_(
        Landmark.id == landmark_id,
        Landmark.user_id == user.id
    )).first()

    if not lm:
        raise ValueError("Landmark not found")
    
    p = Photo(os.path.join("uploads", filename), user.id, lm.id)
    os.mkdir("uploads")
    db.session.add(p)
    db.session.commit()
    photo.save(p.url)
