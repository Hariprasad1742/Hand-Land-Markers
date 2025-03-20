

# Hand Landmark Detection System

## Overview
This project implements a **Hand Landmark Detection System** using **MediaPipe** and **OpenCV**. It detects hand landmarks (e.g., fingertips, joints) in real-time from a webcam feed or a pre-recorded video. The application provides a **Streamlit-based UI** for interactive use and a standalone OpenCV script for direct execution.

## Features
- **Real-time hand landmark detection** using **MediaPipe Hands**.
- **Streamlit-based web UI** for video processing and webcam interaction.
- **Highlights key hand landmarks**, including **fingertips (green)** and **hand edges (blue)**.
- **Standalone OpenCV script** for direct webcam-based hand tracking.
- **Supports both uploaded videos and live webcam streams**.

## Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/hand-landmark-detection.git
cd hand-landmark-detection

2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

Usage
1️⃣ Run the Streamlit App

streamlit run app.py

Then, open the provided localhost URL in your browser.
2️⃣ Run the OpenCV Standalone Script

python Hand_Landmark_detection.py

![hand1](https://github.com/user-attachments/assets/947ad61b-c2ef-4d26-94e2-cd54d5f0d574)
![hand3](https://github.com/user-attachments/assets/a97c54fc-e513-4550-97fe-d6cc4afd6728)
![hand2](https://github.com/user-attachments/assets/d6f39530-2071-4eba-9ab0-f89dd7ed28f8)


