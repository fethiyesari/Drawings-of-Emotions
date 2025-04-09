# figure_size.py
import cv2
import numpy as np

def analyze_figure_size(image_path):
    # Görüntüyü oku ve gri tonlamaya çevir
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Görüntüyü ters çevir
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    # Konturları tespit et
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # En büyük figürün boyutlarını ölç
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area

    # Psikolojik analiz - Büyük figür = özgüven
    if max_area > 5000:  # Bu eşik değerini isteğe göre ayarlayabilirsiniz
        return "Confidence"
    else:
        return "Shyness"
