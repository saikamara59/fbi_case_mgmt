import face_recognition
import numpy as np

def extract_face_encoding(image_bytes):
    image = face_recognition.load_image_file(image_bytes)
    encodings = face_recognition.face_encodings(image)
    return encodings[0] if encodings else None

def compare_faces(known_encodings, unknown_encoding, tolerance=0.6):
    distances = face_recognition.face_distance(known_encodings, unknown_encoding)
    matches = distances <= tolerance
    return matches, distances
