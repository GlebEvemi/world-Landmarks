from app import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmark.id'))

    def __init__(self, url, user_id, landmark_id):
        self.url = url, 
        self.user_id = user_id,
        self.landmark_id = landmark_id        

    def __repr__(self):
        return f"Photo lol"
