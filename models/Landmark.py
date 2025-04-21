from app import db

class Landmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(254), unique=True, nullable=False)
    location = db.Column(db.String(256), nullable=False)
    country = db.Column(db.String(256), nullable=False)
    image_url = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description, location, country, image_url, user_id):
        self.name = name
        self.description = description
        self.location = location
        self.country=country
        self.image_url = image_url
        self.user_id = user_id
        

    def __repr__(self):
        return f"landmark lol"