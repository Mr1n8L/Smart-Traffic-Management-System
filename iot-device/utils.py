def preprocess_image(image):
    import cv2
    import numpy as np
    img = cv2.resize(image, (64, 64))
    img = img.astype('float32') / 255
    return np.expand_dims(img, axis=0)
