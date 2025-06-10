from app import db
from models.User import User


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmark.id'))
    comment = db.Column(db.String(256), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('landmark_id', 'user_id', name='uix_landmark_user'),
    )

    def __init__(self, rating, user_id, landmark_id, comment):
        self.rating = rating
        self.user_id = user_id
        self.landmark_id = landmark_id
        self.comment = comment


    def to_dict(self):
        user: User = User.query.filter_by(id=self.user_id).first()

        return {
            "id": self.id,
            "rating": self.rating,
            "user": {
                    "id": user.id,
                    "name": user.username,
            },
            "comment": self.comment,
        }
