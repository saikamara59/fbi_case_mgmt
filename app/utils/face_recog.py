import face_recognition
from io import BytesIO
import numpy as np

def extract_face_encoding(image_bytes):
    try:
        image = face_recognition.load_image_file(BytesIO(image_bytes))
        encodings = face_recognition.face_encodings(image)
        return encodings[0] if encodings else None
    except Exception as e:
        print("Face encoding error:", e)
        return None

def compare_faces(known_encodings, unknown_encoding, tolerance=0.6):
    results = face_recognition.compare_faces(known_encodings, unknown_encoding, tolerance)
    distances = face_recognition.face_distance(known_encodings, unknown_encoding)
    return results, distances
