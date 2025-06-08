import os
from sqlalchemy import and_
from werkzeug.datastructures import FileStorage
from models.Landmark import Landmark
from models.Photo import Photo
from models.User import User
from app import db


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
    )).first()

    if not lm:
        raise ValueError("Landmark not found")
    
    p = Photo(os.path.join("uploads", filename), user.id, lm.id)
    os.makedirs("uploads", exist_ok=True)
    db.session.add(p)
    db.session.commit()
    photo.save(p.url)


def delete_photo(
    landmark_id: int,
    photo_id: int,
    user: User,
):
    if not user:
        raise ValueError("Unauthorized")

    lm: Landmark = Landmark.query.filter(and_(
        Landmark.id == landmark_id,
        Landmark.user_id == user.id
    )).first()

    if not lm:
        raise ValueError("Landmark not found")
    photo: Photo = Photo.query.filter(and_(
        Photo.id == photo_id,
        Photo.user_id == user.id,
    )).first()
    os.remove(os.path.join("uploads",))

    db.session.delete(photo)
    db.session.commit()
    
   
def get_landmark_photos(landmark_id: int) -> list[Photo]:
    photos: Photo = Photo.query.filter_by(
        landmark_id=landmark_id,
    ).all()

    return photos
