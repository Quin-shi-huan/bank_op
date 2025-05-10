from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.fisic_person_routes import fisic_person_route_bp
from src.main.routes.juridic_person_routes import juridic_person_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(fisic_person_route_bp)
app.register_blueprint(juridic_person_route_bp)
