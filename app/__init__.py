from flask import Flask
from flask_cors import CORS


from app.routes.auth_routes import auth_bp
from app.routes.case_routes import case_bp
from app.routes.face_routes import face_bp
from app.routes.suspect_routes import suspect_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register all blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(case_bp, url_prefix="/api/cases")
    app.register_blueprint(face_bp, url_prefix="/api/face")
    app.register_blueprint(suspect_bp, url_prefix="/api/suspects")

    return app
