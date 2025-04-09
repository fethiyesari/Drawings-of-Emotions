# line_thickness.py
import cv2
import numpy as np

def analyze_line_thickness(image_path):
    # Görüntüyü oku ve gri tonlamaya çevir
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Kenarları tespit etmek için Canny algoritması kullanma
    edges = cv2.Canny(image, 100, 200)

    # Kenarların kalınlıklarını ölçme
    thickness = np.sum(edges) / 255  # Kenarların toplam yoğunluğunu al

    # Psikolojik analiz - Kalın çizgiler öfke/gerilim
    if thickness > 5000:  # Bu eşik değerini isteğe göre ayarlayabilirsiniz
        return "Anger"
    else:
        return "Calm"
