import face_recognition
import numpy as np
from io import BytesIO

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

def compare_faces(known_encodings, unknown_encoding, tolerance=0.6):
    try:
        # Calculate distances between the unknown encoding and known encodings
        distances = face_recognition.face_distance(known_encodings, unknown_encoding)

        # Determine matches based on the tolerance
        matches = distances <= tolerance

        # Debugging: Print distances and matches
        print("Distances:", distances)
        print("Matches:", matches)

        return matches, distances
    except Exception as e:
        print("Error in compare_faces:", e)
        return [], []

