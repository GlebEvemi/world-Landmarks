from sqlalchemy import and_
from models.Landmark import Landmark
from models.User import User
from app import db


def create_landmark(
        user: User, 
        name: str, 
        description: str, 
        location: str, 
        country: str
) -> Landmark:
    if not user:
        raise ValueError("Unauthorized")
    existing = Landmark.query.filter_by(name=name).first()

    if existing:
        raise ValueError("This landmark exists")

    lm = Landmark(name, description, location, country, user.id)

    db.session.add(lm)
    db.session.commit()

    return lm


def delete_landmark(user: User, id: int):
    if not user:
        raise ValueError("Unauthorized")

    lm: Landmark = Landmark.query.filter(and_(
        Landmark.id == id,
        Landmark.user_id == user.id
    )).first()
    if not lm:
        raise ValueError("Landmark not found")
    db.session.delete(lm)
    db.session.commit()


def update_landmark(
        user: User, 
        name: str, 
        description: str, 
        location: str, 
        country: str,
        id: int
) -> Landmark:
    if not user:
        raise ValueError("Unauthorized")
    lm: Landmark = Landmark.query.filter(and_(
        Landmark.id == id,
        Landmark.user_id == user.id
    )).first()

    if not lm:
        raise ValueError("Landmark not found")
    
    lm.name = name
    lm.description = description
    lm.country = country
    lm.location = location

    db.session.commit()
    
    return lm


def list_landmarks(sort_by=None, country_filter=None) -> list[Landmark]:
    if not sort_by:
        sort_by = Landmark.id

    query = Landmark.query

    if country_filter:
        query = query.filter(Landmark.country.like(f"%{country_filter}%"))

    if sort_by:
        query = query.order_by(sort_by)

    return query.all()


def get_landmark_by_id(id: int) -> Landmark:
    return Landmark.query.filter_by(id=id).first()
