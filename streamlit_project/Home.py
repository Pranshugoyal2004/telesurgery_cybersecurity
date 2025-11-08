import streamlit as st
import pandas as pd
df= pd.read_csv("telesurgery_cybersecurity_dataset.csv")

st.title("Cybersecurity in Telesurgery ")
st.subheader("🧠 Project Overview")
st.text("""This project explores the application of data science techniques to enhance cybersecurity in robotic telesurgery systems operating over 5G networks. Telesurgery enables surgeons to perform operations remotely via robotic arms, but such systems are vulnerable to cybersecurity threats due to their reliance on real-time, high-speed data transmission.

The dataset used in this project is structured to simulate cybersecurity risk scenarios during telesurgery operations, focusing on communication between robotic systems and surgeons across potentially insecure networks. It includes critical data such as robotic gestures, encryption status, communication parameters, and network metrics—all of which influence the detection and severity of cyber threats.

This project is designed to support researchers, developers, and cybersecurity professionals working on improving the reliability and safety of remote robotic surgery systems.""")

st.subheader("Dataset")
st.dataframe(df)
st.subheader("📊 Dataset Overview")
st.text("The dataset consists of 1,000 rows and 18 columns related to cybersecurity and robotic gestures in a telesurgery environment. Here's a breakdown of each column:")
data = {
    "Column_Name":[
        'Robot_Gesture_ID',
        'Gesture_Type',
        'Gesture_Coordinates_(x, y, z)',
        'Timestamp',
        'Gesture_Duration_(sec)',
        'Robot_Status',
        'Message_ID',
        'Sender',
        'Receiver',
        'Encryption_Algorithm_Used',
        'Encryption_Status',
        'Network_Latency_(ms)',
        'Data_Transfer_Rate_(Mbps)',
        'Threat_Type',
        'Threat_Severity',
        'Response_Time_(sec)',
        'Response_Action_Taken',
        'Threat_Detected'
    ],
    "Description": [
        'Unique identifier for each robot gesture.',
        'Type of gesture performed (e.g., Incision, Diagnosis, Suturing).',
        '3D coordinates where the gesture occurred; stored as a string.',
        'Time the gesture or activity was recorded.',
        'Duration of the gesture in seconds.',
        'Status of the robot during gesture (e.g., Active, Idle).',
        'ID of the message exchanged between robot and operator.',
        'Who sent the message (e.g., Robot or Operator).',
        'Who received the message.',
        'Type of encryption algorithm used (e.g., Two Fish).',
        'Whether the data was encrypted or not.',
        'Delay in data transmission in milliseconds.',
        'Speed of data transfer during gesture.',
        'Type of cybersecurity threat detected.',
        'Severity of the detected threat (e.g., Low, High).',
        'Time taken to respond to a threat.',
        'Action taken in response to the detected threat.',
        'Binary flag (1 = Threat detected, 0 = No threat).',
    ],
    "Data_Types": [
        'int64',
        'object',
        'object',
        'object',
        'float64',
        'object',
        'int64',
        'object',
        'object',
        'object',
        'object',
        'int64',
        'int64',
        'object',
        'object',
        'float64',
        'object',
        'int64',
    ]
}

df2 = pd.DataFrame(data)
st.dataframe(df2)

st.text("To download the dataset:")
st.link_button("Click me","https://www.kaggle.com/code/devraai/cybersecurity-threat-detection-in-telesurgery/input", use_container_width=True)



