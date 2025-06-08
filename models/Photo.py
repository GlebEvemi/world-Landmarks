from sqlalchemy.engine import url
from app import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmark.id'))

    def __init__(self, url, user_id, landmark_id):
        self.url = url, 
        self.user_id = user_id,
        self.landmark_id = landmark_id        

    
    def to_dict(self, host: str):
        return {
            "url": f"{host}{self.url}",
            "id": self.id
        }
