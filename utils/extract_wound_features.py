from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def extract_wound_features(image_path):
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    
    features = ['Wound Color: Red', 
                'Wound Color: Purple', 
                'Wound Color: Yellow', 
                'Wound Color: White', 
                'Wound Color: Black', 
                'Presence of Pus', 
                'Presence of Scab', 
                'Wound Swelling', 
                'Wound Temperature: Warm', 
                'Wound Temperature: Normal', 
                'Wound Odor: Unpleasant', 
                'Wound Odor: Neutral', 
                'Wound Moisture: Dry', 
                'Wound Moisture: Moist', 
                'Wound Texture: Smooth', 
                'Wound Texture: Rough', 
                'Pain Level: High', 
                'Pain Level: Low', 
                'Wound Depth: Superficial', 
                'Wound Depth: Partial Thickness', 
                'Wound Depth: Full Thickness', 
                'Wound Edges: Regular', 
                'Wound Edges: Irregular', 
                'Wound Edges: Undermined', 
                'Skin Color: Normal', 
                'Skin Color: Hyperpigmented', 
                'Skin Color: Hypopigmented', 
                'Skin Integrity: Intact', 
                'Skin Integrity: Fragile', 
                'Skin Integrity: Inflamed',]
    
    # Generate feature scores
    feature_scores = {}
    for desc in features:
        text_inputs = processor(text=desc, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            text_features = model.get_text_features(**text_inputs)
        similarity = torch.matmul(image_features, text_features.T)
        feature_scores[desc] = similarity.item()
    
    return feature_scores