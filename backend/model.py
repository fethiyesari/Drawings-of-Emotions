# model.py
import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Özellikleri çıkarmak için kullanacağımız yardımcı fonksiyonlar
from feature_engineering.color_analysis import analyze_color
from feature_engineering.line_thickness import analyze_line_thickness
from feature_engineering.space_usage import analyze_space_usage
from feature_engineering.figure_size import analyze_figure_size
from feature_engineering.face_expression import analyze_face_expression

# Etiketlerin ve resimlerin bulunduğu dizinler
image_dir = 'backend/labeled_images'

# Her bir duygunun etiketleri
emotions = ['angry', 'fear', 'happy', 'sad']

def extract_features_and_labels():
    features = []
    labels = []

    for emotion in emotions:
        emotion_dir = os.path.join(image_dir, emotion)
        for image_file in os.listdir(emotion_dir):
            if image_file.endswith('.jpeg'):
                image_path = os.path.join(emotion_dir, image_file)
                
                # Her resim için özellikleri çıkaralım
                color = analyze_color(image_path)
                line_thickness = analyze_line_thickness(image_path)
                space_usage = analyze_space_usage(image_path)
                figure_size = analyze_figure_size(image_path)
                face_expression = analyze_face_expression(image_path)
                
                # Özellikler
                feature_vector = [color == "Happiness", line_thickness == "Anger",
                                  space_usage == "Introversion", figure_size == "Confidence", 
                                  face_expression == "Happiness"]

                features.append(feature_vector)
                labels.append(emotion)

    return np.array(features), np.array(labels)

# Veriyi hazırlama
X, y = extract_features_and_labels()

# Etiketleri sayısal değerlere dönüştürme
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Veriyi eğitim ve test için bölelim
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Modeli oluşturma
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(4, activation='softmax'))  # 4 sınıf için softmax çıkışı

# Modeli derleyelim
model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Modeli eğitelim
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Modeli kaydedelim
model.save('emotion_detection_model.h5')

# Modeli değerlendirme
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')
print(f'Test Accuracy: {accuracy}')
