import streamlit as st
from mediapipe_pose_detection import mediapipe_pose_detection

# Add navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "MediaPipe Pose Detection"])

# Home page
if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the home page.")

# MediaPipe Pose Detection page
elif page == "MediaPipe Pose Detection":
    mediapipe_pose_detection()
