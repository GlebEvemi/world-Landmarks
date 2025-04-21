from app import db


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmark.id'))

    def __init__(self, rating, user_id, landmark_id):
        self.raing = rating
        self.user_id = user_id
        self.landmark_id = landmark_id

    def __repr__(self):
        return f"Rating"