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

![GUI Interface](assets/gui_interface.png)

### Classification Output
An example of the output showing the waste type and its recommended bin:

![Output Example](assets/output_example.png)

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries:
  ```bash
  pip install opencv-python-headless cvzone pillow
