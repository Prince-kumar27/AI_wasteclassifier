# Waste Classifier Using Tkinter and CVZone

This project is a **Waste Classification System** that leverages machine learning and computer vision to classify waste into different categories (e.g., glass, plastic, paper) and provides recommendations for appropriate recycling bins. The user interacts with the system through a graphical user interface (GUI) built using **Tkinter**, while the waste classification is powered by a trained **TensorFlow/Keras** model integrated with **CVZone**.

---

## Features

- **User-Friendly GUI**: Easy-to-use interface for waste classification and recycling guidance.
- **AI-Powered Classification**: Uses a trained deep learning model to classify waste.
- **Visual Feedback**: Displays the waste category and highlights the corresponding bin with overlaid images.
- **File Selection**: Allows users to browse and select waste images for analysis.

---

## Demo

### GUI Interface
The graphical user interface where users can upload and classify waste images:

![GUI Interface](https://github.com/user-attachments/assets/503ee77c-c1a6-48a7-be63-b4ecc16507b6)



### Classification Output
An example of the output showing the waste type and its recommended bin:

![Output Example](https://github.com/user-attachments/assets/1b00a446-a51c-4fbe-905f-619ef8f521f5)


---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries:
  ```bash
  pip install opencv-python-headless cvzone pillow
