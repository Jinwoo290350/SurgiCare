import keras
from keras.preprocessing import image
import streamlit as st
import numpy as np
import requests
import os

def download_model(model_url, model_path='temp_model.keras'):
    # Download the model if it doesn't exist locally
    if not os.path.exists(model_path):
        print(f"Downloading model from {model_url}...")
        response = requests.get(model_url)
        if response.status_code == 200:
            with open(model_path, 'wb') as file:
                file.write(response.content)
            print("Model downloaded and saved.")
        else:
            raise Exception(f"Failed to download model. Status code: {response.status_code}")
    return model_path

def extract_wound_class(img_path, model_name):
    
    if model_name == 'SurgiCare-V1-fast-best':
        model_url = 'https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-fast-best.keras'
        image_size = 224
        
    elif model_name == 'SurgiCare-V1-mini-best':
        model_url = 'https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-mini-best-model.keras'
        image_size = 224
    
    elif model_name == 'SurgiCare-V1-best':
        model_url = 'https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-best.keras'
        image_size = 300
        
    # Define class labels
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
    
    # Download and load the model
    model_path = download_model(model_url, model_path=model_name + '.keras')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_name + '.keras'}")

    print(f"Loading model from {model_path}...")
    best_model = keras.models.load_model(model_path)  # Changed to models.load_model
    print("Model loaded successfully.")
    
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(image_size, image_size))  # Now using 224x224
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Predict the class
    try:
        predictions = best_model.predict(img_array)
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")
        return None  # Or handle the error in an appropriate way
    predicted_index = np.argmax(predictions)
    
    # Exclude Laseration if predicted
    # if predicted_index == 5:
    #     second_highest_index = np.argsort(predictions[0])[-2]
    #     predicted_index = second_highest_index
    
    predicted_class = class_labels[predicted_index]

    return predicted_class