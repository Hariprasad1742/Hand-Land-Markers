import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import tempfile

# Initialize MediaPipe Hands once (improves performance)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

st.title("Hand Landmark Detection")

# Function to detect hand landmarks and highlight fingertips & edges
def detect_hand_landmarks(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            h, w, _ = frame.shape

            for idx, landmark in enumerate(hand_landmarks.landmark):
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                # Fingertips (Green)
                if idx in [4, 8, 12, 16, 20]:
                    cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)
                # Key Edges (Blue)
                elif idx in [0, 5, 9, 13, 17]:
                    cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)

    return frame

# Video Processing
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_hand_landmarks(frame)
        stframe.image(frame, channels="BGR", use_container_width=True)

    cap.release()

# Streamlit Options
option = st.radio("Choose an option:", ("Upload a Video", "Use Webcam"))

if option == "Upload a Video":
    uploaded_file = st.file_uploader("Upload a video...", type=["mp4", "avi", "mov"])
    
    if uploaded_file:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_file.write(uploaded_file.read())
        process_video(temp_file.name)

elif option == "Use Webcam":
    run_webcam = st.checkbox("Start Webcam")

    if run_webcam:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while run_webcam:
            ret, frame = cap.read()
            if not ret:
                st.write("Error: Unable to capture video.")
                break

            frame = detect_hand_landmarks(frame)
            stframe.image(frame, channels="BGR", use_container_width=True)

        cap.release()
