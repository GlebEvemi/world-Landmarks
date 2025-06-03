from app import app, db
from models import Landmark, User, Rating, Photo
import pymysql
from flask_swagger_ui import get_swaggerui_blueprint
pymysql.install_as_MySQLdb()


SWAGGER_URL = '/api/docs'
API_URL = 'http://localhost:5000/swagger.json'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  
        API_URL,
        config={ 
            'app_name': "World Landmarks"
        },
    )
    app.register_blueprint(swaggerui_blueprint)

    app.run(debug=True, host='0.0.0.0')


