from app import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable = False)
    description = db.Column(db.String(254), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmark.id'))

    def __init__(self, url, description, user_id, landmark_id):
        self.url = url, 
        self.description = description, 
        self.user_id = user_id,
        self.landmark_id = landmark_id        

    def __repr__(self):
        return f"Photo lol"
