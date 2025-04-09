# color_analysis.py
import cv2
import numpy as np
from sklearn.cluster import KMeans

def analyze_color(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Görüntüyü yeniden boyutlandırarak renkleri daha kolay işleyebilir hale getirelim
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # KMeans ile ana renkleri bulma
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(image)
    dominant_colors = kmeans.cluster_centers_

    # Renk analizi - sıcak renkler vs koyu renkler
    color_scores = {"warm": 0, "cool": 0}
    for color in dominant_colors:
        r, g, b = color
        if r > g and r > b:
            color_scores["warm"] += 1
        else:
            color_scores["cool"] += 1

    # Psikolojik analiz - Mutluluk ve kaygı arasında bir ilişki
    if color_scores["warm"] > color_scores["cool"]:
        return "Happiness"
    else:
        return "Anxiety"
