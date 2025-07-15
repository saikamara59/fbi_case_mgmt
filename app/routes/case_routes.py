from flask import Blueprint, jsonify, request
from app.db import get_db_connection

case_bp = Blueprint("case_bp", __name__)

@case_bp.route("/", methods=["GET"])
def get_cases():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, description, status, created_at FROM cases")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        cases = []
        for row in rows:
            cases.append({
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "status": row[3],
                "created_at": row[4].isoformat() if row[4] else None
            })
        return jsonify(cases), 200
    except Exception as e:
        print("Error fetching cases:", e)
        return jsonify({"error": "Could not fetch cases"}), 500

@case_bp.route("/", methods=["POST"])
def create_case():
    try:
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        status = data.get("status", "open")

        if not title:
            return jsonify({"error": "Title is required"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cases (title, description, status) VALUES (%s, %s, %s) RETURNING id",
            (title, description, status)
        )
        case_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Case created", "case_id": case_id}), 201
    except Exception as e:
        print("Error creating case:", e)
        return jsonify({"error": "Could not create case"}), 500

