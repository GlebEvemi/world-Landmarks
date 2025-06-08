from app import app, db
from models import Landmark, User, Rating, Photo
import app.user
import app.landmark
import app.photo
import pymysql
from flask_swagger_ui import get_swaggerui_blueprint
pymysql.install_as_MySQLdb()


SWAGGER_URL = '/api/docs'
API_URL = '/apispec_1.json'

if __name__ == '__main__':
    with app.app.app_context():
        db.create_all()
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  
        API_URL,
        config={ 
            'app_name': "World Landmarks"
        },
    )
    app.app.register_blueprint(swaggerui_blueprint)

    app.app.run(debug=True, host='0.0.0.0')


