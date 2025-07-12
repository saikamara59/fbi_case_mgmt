from flask import Blueprint, request, jsonify
from app.utils.face_recog import extract_face_encoding, compare_faces
from app.db import get_db_connection
import numpy as np

face_bp = Blueprint("face", __name__)

# Upload and store a suspect's face
@face_bp.route("/add-suspect-face/<int:suspect_id>", methods=["POST"])
def add_suspect_face(suspect_id):
    if 'image' not in request.files:
        return jsonify({"error": "Image required"}), 400

    file = request.files['image']
    image_bytes = file.read()
    encoding = extract_face_encoding(image_bytes)

    if encoding is None:
        return jsonify({"error": "No face found"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO suspect_faces (suspect_id, encoding) VALUES (%s, %s)",
        (suspect_id, encoding.tobytes())
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Face encoding saved"}), 201

# Compare uploaded image against all stored suspect faces
@face_bp.route("/match-face", methods=["POST"])
def match_face():
    if 'image' not in request.files:
        return jsonify({"error": "Image required"}), 400

    file = request.files['image']
    image_bytes = file.read()

    unknown_encoding = extract_face_encoding(image_bytes)
    if unknown_encoding is None:
        return jsonify({"error": "No face detected"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT suspect_id, encoding FROM suspect_faces")
    data = cur.fetchall()
    cur.close()
    conn.close()

    known_encodings = [np.frombuffer(row[1], dtype=np.float64) for row in data]
    suspect_ids = [row[0] for row in data]

    matches, distances = compare_faces(known_encodings, unknown_encoding)

    response = []
    for i, match in enumerate(matches):
        if match:
            response.append({
                "suspect_id": suspect_ids[i],
                "confidence": float(1 - distances[i])
            })

    return jsonify({"matches": response}), 200
