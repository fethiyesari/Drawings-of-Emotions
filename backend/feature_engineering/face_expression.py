# face_expression.py
import cv2
from deepface import DeepFace

def analyze_face_expression(image_path):
    # Yüz tanıma ve duygu analizi
    try:
        result = DeepFace.analyze(image_path, actions=['emotion'])
        dominant_emotion = result[0]['dominant_emotion']

        # Pozitif duygu - gülümseme
        if dominant_emotion == "happy":
            return "Happiness"
        else:
            return "Neutral"
    except Exception as e:
        return "No face detected"
