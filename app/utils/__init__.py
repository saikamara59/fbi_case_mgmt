from app.routes.face_routes import face_bp

def create_app():
    app = Flask(__name__)
    # ... other blueprints
    app.register_blueprint(face_bp, url_prefix="/api/face")
    return app
