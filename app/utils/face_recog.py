import face_recognition
import numpy as np
from io import BytesIO

def extract_face_encoding(image_bytes):
    # ✅ Wrap the bytes in a file-like object
    image_file = BytesIO(image_bytes)
    image = face_recognition.load_image_file(image_file)
    encodings = face_recognition.face_encodings(image)
    return encodings[0] if encodings else None

def compare_faces(known_encodings, unknown_encoding, tolerance=0.6):
    distances = face_recognition.face_distance(known_encodings, unknown_encoding)
    matches = distances <= tolerance
    return matches, distances

