# Surgicare

> Surgicare (Surgical + Care) 
![](https://imgur.com/a/surgicare-logo-uteaCTW.png)

SurgiCare is an AI system designed to support post-surgery patient recovery. In this repository, we focus on a wound classification model trained on an open-source dataset. Our objective is to improve the accuracy of wound detection and guide patients in managing their wound recovery efficiently.

- **Online Demo**: [https://surgicare-demo.streamlit.app/](https://surgicare-demo.streamlit.app/)
- Wound dataset: [https://www.kaggle.com/datasets/ibrahimfateen/wound-classification](https://www.kaggle.com/datasets/ibrahimfateen/wound-classification))

- Model Hub: [https://huggingface.co/PogusTheWhisper/SurgiCare](https://huggingface.co/PogusTheWhisper/SurgiCare)
- Pretrained Models:
    * Surgicare-V1-best: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-best.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-best.keras)
    * Surgicare-V1-fast: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-mini-best-model.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-mini-best-model.keras)
    * Surgicare-V1-mini: [https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-mini-best-model.keras](https://huggingface.co/PogusTheWhisper/SurgiCare/resolve/main/SurgiCare-V1-mini-best-model.keras)

## Result of training!!
### Efficientnet B3
* Accuracy: 0.9062 Approximately 11 seconds per image.
* I used EfficientNet-B3 to train for 25 epochs, monitoring the validation loss.

![alt text](wound_classify_train/SurgiCare-V1-best.png?raw=true)

### MobileNetV3Large
* Accuracy: 0.7969 Approximately 5 seconds per image.
* I used MobileNetV3Large to train for 50 epochs, monitoring the validation loss.
  
![alt text](wound_classify_train/SurgiCare-V1-fast.png?raw=true)

### MobileNetV3Small
* Accuracy: 0.7812 Approximately 4 seconds per image.
* I used MobileNetV3Small to train for 50 epochs, monitoring the validation loss.
  
![alt text](wound_classify_train/SurgiCare-V1-mini.png?raw=true)
