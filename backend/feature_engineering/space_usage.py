# space_usage.py
import cv2
import numpy as np

def analyze_space_usage(image_path):
    # Görüntüyü oku ve gri tonlamaya çevir
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Görüntüyü ters çevir (beyaz arka plan, siyah çizimler)
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    # Konturları tespit et
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # En dıştaki figürün merkezi
    x, y, w, h = cv2.boundingRect(contours[0])
    center_x = x + w // 2
    center_y = y + h // 2

    # Görüntü boyutları
    height, width = image.shape

    # Köşeye yakınlık
    if center_x < width // 4 or center_y < height // 4:
        return "Introversion"
    else:
        return "Extroversion"
