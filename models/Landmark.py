from app import db

class Landmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(254), unique=True, nullable=False)
    location = db.Column(db.String(256), nullable=False)
    country = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description, location, country, user_id):
        self.name = name
        self.description = description
        self.location = location
        self.country = country
        self.user_id = user_id
 
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "country": self.country,
            "user_id": self.user_id
        }

    def to_dict_summary(self):
        return {
        "id": self.id,
        "country": self.country,
        "name": self.name,
    }
