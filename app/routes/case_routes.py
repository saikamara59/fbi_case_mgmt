from flask import Blueprint

case_bp = Blueprint("case", __name__)

# Optional: add a test route so you know it works
@case_bp.route("/")
def test():
    return {"message": "Case routes are working!"}
