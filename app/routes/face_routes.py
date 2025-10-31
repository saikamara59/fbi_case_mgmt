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

from io import BytesIO
import face_recognition

def extract_face_encoding(image_bytes):
    try:
        # Wrap the bytes in a file-like object
        image_file = BytesIO(image_bytes)
        image = face_recognition.load_image_file(image_file)

        # Debugging: Check if the image is loaded
        print("Image loaded successfully. Shape:", image.shape)

        # Detect face encodings
        encodings = face_recognition.face_encodings(image)

        # Debugging: Check if any faces are detected
        if not encodings:
            print("No faces detected in the image.")
        else:
            print(f"Number of faces detected: {len(encodings)}")

        return encodings[0] if encodings else None
    except Exception as e:
        print("Error in extract_face_encoding:", e)
        return None
