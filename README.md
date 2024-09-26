# Surgicare

> Surgicare (Surgical + Care) 
<img src="https://i.imgur.com/nOi95Cj.png" width="250">

SurgiCare is an AI system designed to support post-surgery patient recovery. In this repository, we focus on a wound classification model trained on an open-source dataset. Our objective is to improve the accuracy of wound detection and guide patients in managing their wound recovery efficiently.

- **Online Demo**: [https://surgicare-demo.streamlit.app/](https://surgicare-demo.streamlit.app/)
- Wound dataset: [https://www.kaggle.com/datasets/ibrahimfateen/wound-classification](https://www.kaggle.com/datasets/ibrahimfateen/wound-classification)

- Model Hub: [https://huggingface.co/PogusTheWhisper/SurgiCare](https://huggingface.co/PogusTheWhisper/SurgiCare)
- Pretrained Models:
    * Surgicare-V1-best: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-large.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-**large.keras)
    * Surgicare-V1-fast: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-medium.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-medium.keras)
    * Surgicare-V1-mini: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-small.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-small.keras)

## Result of standard model
### Efficientnet B3
* Accuracy: 0.6884

![alt text](wound_classify_train/EfficientNetV2B3-standard.png?raw=true)

### MobileNetV3Large
* Accuracy: 0.6164
  
![alt text](wound_classify_train/MobileNetV3Large-standard.png?raw=true)

### MobileNetV3Small
* Accuracy: 0.6199
  
![alt text](wound_classify_train/MobileNetV3Small-standard.png?raw=true)

## Result of our training!!
### EfficientnetV2 B3
* Accuracy: 0.9127
* I used EfficientNet-B3 to train for 50 epochs, monitoring the validation loss.

![alt text](wound_classify_train/SurgiCare-V1-large-turbo.png?raw=true)
### Efficientnet B3
* Accuracy: 0.9062
* I used EfficientNet-B3 to train for 25 epochs, monitoring the validation loss.

![alt text](wound_classify_train/SurgiCare-V1-large.png?raw=true)

### MobileNetV3Large
* Accuracy: 0.7969
* I used MobileNetV3Large to train for 50 epochs, monitoring the validation loss.
  
![alt text](wound_classify_train/SurgiCare-V1-medium.png?raw=true)

### MobileNetV3Small
* Accuracy: 0.7812
* I used MobileNetV3Small to train for 50 epochs, monitoring the validation loss.
  
![alt text](wound_classify_train/SurgiCare-V1-small.png?raw=true)
