import keras
from keras.preprocessing import image
import numpy as np

def extract_wound_class(img_path, model_path='wound_classify_train/Surgicare_V1_best_model.keras'):
    class_labels = {0: 'Abrasions',
                    1: 'Bruises',
                    2: 'Burns',
                    3: 'Cut',
                    4: 'Diabetic Wounds',
                    5: 'Laseration',
                    6: 'Normal',
                    7: 'Pressure Wounds',
                    8: 'Surgical Wounds',
                    9: 'Venous Wounds'}
    best_model = keras.saving.load_model(model_path)
    
    img = image.load_img(img_path, target_size=(300, 300))  # Match model's input size

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    predictions = best_model.predict(img_array)

    predicted_index = np.argmax(predictions)
    
    if predicted_index == 5:
        # Don't include Laseration
        second_highest_index = np.argsort(predictions[0])[-2]
        predicted_index = second_highest_index
    
    predicted_class = class_labels[predicted_index]

    return predicted_class
