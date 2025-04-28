import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('../model/ambulance_detector_model.h5')

def predict_ambulance(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))
    img = img.astype('float32') / 255
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    return prediction[0][0] > 0.5

if __name__ == "__main__":
    from camera_feed import capture_frame

    capture_frame()
    if predict_ambulance('captured_frame.jpg'):
        print("🚑 Ambulance detected!")
    else:
        print("No ambulance detected.")
