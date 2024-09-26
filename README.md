# Surgicare

> Surgicare (Surgical + Care) 
<img src="https://i.imgur.com/nOi95Cj.png" width="250">

SurgiCare is an AI system designed to support post-surgery patient recovery. In this repository, we focus on a wound classification model trained on an open-source dataset. Our objective is to improve the accuracy of wound detection and guide patients in managing their wound recovery efficiently.

- **Online Demo**: [https://surgicare-demo.streamlit.app/](https://surgicare-demo.streamlit.app/)
- Wound dataset: [https://www.kaggle.com/datasets/ibrahimfateen/wound-classification](https://www.kaggle.com/datasets/ibrahimfateen/wound-classification)

- Model Hub: [https://huggingface.co/PogusTheWhisper/SurgiCare](https://huggingface.co/PogusTheWhisper/SurgiCare)
- Pretrained Models:
    * Surgicare-V1-large-turbo: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-large-turbo.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-large-turbo.keras)
    * Surgicare-V1-large: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-large.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-large.keras)
    * Surgicare-V1-medium: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-medium.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-medium.keras)
    * Surgicare-V1-small: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-small.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-small.keras)

---

## Result of standard models
### EfficientnetV2 B3
* Accuracy: 0.6884

<img src="wound_classify_train/EfficientNetV2B3-standard.png?raw=true" width="800">

### Efficientnet B3
* Accuracy: 0.7436

<img src="wound_classify_train/EfficientNetB3-standard.png?raw=true" width="800">

### MobileNetV3Large
* Accuracy: 0.6164
  
<img src="wound_classify_train/MobileNetV3Large-standard.png?raw=true" width="800">

### MobileNetV3Small
* Accuracy: 0.6199
  
<img src="wound_classify_train/MobileNetV3Small-standard.png?raw=true" width="800">

---

## Result of our models!!
### EfficientnetV2 B3
* Accuracy: 0.9127
* Training Details: I used EfficientNet-B3 to train for 50 epochs, monitoring the validation loss.
  
<img src="wound_classify_train/SurgiCare-V1-large-turbo.png?raw=true" width="800">

### Efficientnet B3
* Accuracy: 0.9062
* Training Details: I used EfficientNet-B3 to train for 25 epochs, monitoring the validation loss.

<img src="wound_classify_train/SurgiCare-V1-large.png?raw=true" width="800">

### MobileNetV3Large
* Accuracy: 0.7969
* Training Details: I used MobileNetV3Large to train for 50 epochs, monitoring the validation loss.

<img src="wound_classify_train/SurgiCare-V1-medium.png?raw=true" width="800">

### MobileNetV3Small
* Accuracy: 0.7812
* Training Details: I used MobileNetV3Small to train for 50 epochs, monitoring the validation loss.

<img src="wound_classify_train/SurgiCare-V1-small.png?raw=true" width="800">
