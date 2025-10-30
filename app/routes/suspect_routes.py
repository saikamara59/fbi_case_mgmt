# from flask import Blueprint, request, jsonify
# from app.db import get_db_connection

# suspect_bp = Blueprint("suspect_bp", __name__)

# @suspect_bp.route("/", methods=["POST"])
# def add_suspect():
#     data = request.get_json()
#     name = data.get("name")

#     if not name:
#         return jsonify({"error": "Name is required"}), 400

#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO suspects (name) VALUES (%s) RETURNING id",
#             (name,)
#         )
#         new_id = cur.fetchone()[0]
#         conn.commit()
#         cur.close()
#         conn.close()
#         return jsonify({"message": "Suspect added", "suspect_id": new_id}), 201
#     except Exception as e:
#         print("Error inserting suspect:", e)
#         return jsonify({"error": "Failed to insert suspect"}), 500

# # Get all suspects
# @suspect_bp.route("/", methods=["GET"])
# def get_suspects():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id, name, details FROM suspects")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()

#     suspects = [{"id": r[0], "name": r[1], "details": r[2]} for r in rows]
#     return jsonify(suspects), 200


from flask import Blueprint, request, jsonify
from app.db import get_db_connection

suspect_bp = Blueprint("suspect_bp", __name__)

@suspect_bp.route("/", methods=["POST"])
def add_suspect():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO suspects (name) VALUES (%s) RETURNING id",
            (name,)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Suspect added", "suspect_id": new_id}), 201
    except Exception as e:
        print("Error inserting suspect:", e)
        return jsonify({"error": "Failed to insert suspect"}), 500

# Get all suspects
@suspect_bp.route("/", methods=["GET"])
def get_suspects():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, created_at, age, notes, case_id FROM suspects")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    suspects = [
        {
            "id": r[0],
            "name": r[1],
            "created_at": r[2],
            "age": r[3],
            "notes": r[4],
            "case_id": r[5]
        }
        for r in rows
    ]
    return jsonify(suspects), 200