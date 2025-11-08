import streamlit as st
import pandas as pd

st.title("Preprocessing Overview: Telesurgery Cybersecurity Dataset")

df = pd.read_csv("telesurgery_cybersecurity_dataset.csv")

st.markdown("""
This page documents the preprocessing steps applied to the **Telesurgery Cybersecurity Dataset**, including:
- Dropping unnecessary columns
- Handling missing values
- Renaming columns
""")
st.header("1. Renamed Columns")
original_columns = df.columns.tolist()
st.subheader("Original Column Names")
st.write("Robot Gesture ID", "Gesture Type", "Gesture Coordinates (x, y, z)", "Timestamp", "Gesture Duration (sec)", "Robot Status", "Message ID", "Sender", "Receiver", "Encryption Algorithm Used", "Encryption Status", "Network Latency (ms)", "Data Transfer Rate (Mbps)", "Threat Type", "Threat Severity", "Response Time (sec)", "Response Action Taken", "Threat Detected")
renamed_columns = [col.strip().lower().replace(" ", "_") for col in original_columns]
df.columns = renamed_columns


st.subheader("Renamed Column Names")
st.write(df.columns.tolist())

st.header("2. Dropped Columns")

st.markdown("""
The **Timestamp** column was dropped because it was not relevant for downstream analysis or modeling.
""")

st.subheader("Before Dropping Timestamp")
st.write(df.head(5))

if "timestamp" in df.columns:
    df.drop("timestamp", axis=1, inplace=True)

st.subheader("After Dropping `Timestamp`")
st.write(df.head(5))


st.header("3. Handling Missing Values")

st.markdown("""
Missing values in the **Response_Action_Taken** column were filled with the **most frequent value (mode)**.
""")
st.subheader("Missing Values Before Preprocessing")
st.write("Response_Action_Taken missing count:", df["response_action_taken"].isna().sum())

df.fillna({"response_action_taken": df["response_action_taken"].mode()[0]}, inplace=True)

st.subheader("Missing Values After Preprocessing")
st.write("Response_Action_Taken missing count:", df["response_action_taken"].isna().sum())

st.header("Cleaned Dataset Preview")
st.write(df.head())

st.subheader("✅ What This Covers")
st.markdown("- ✔ Dropping of Timestamp")
st.markdown("- ✔ Filling of missing values in Response_Action_Taken")
st.markdown("- All the columns were renamed ")

