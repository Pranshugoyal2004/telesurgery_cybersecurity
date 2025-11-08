import streamlit as st
st.title("Data Exploration")
st.text("The dataset used in this project captures detailed information on robotic telesurgery operations performed over a 5G network, focusing on potential cybersecurity risks. The data was thoroughly examined to understand the nature and distribution of robotic gestures, network performance metrics, encryption status, and threat characteristics. Numerical features such as gesture duration, network latency, data transfer rate, and response time were analyzed to identify patterns and anomalies that could indicate system vulnerabilities. Categorical attributes like gesture type, encryption algorithm used, threat type, and severity were explored to uncover frequent security issues and assess the reliability of communication protocols. Notably, some encryption failures were observed under high latency or low bandwidth conditions, and certain gestures appeared more frequently associated with threat events. These observations helped establish correlations between system behavior and the occurrence of cyber threats, providing valuable insights into areas where security enhancements are necessary.")
st.subheader("🎯 Objectives:")
st.markdown("- Identify common threats and vulnerabilities in telesurgery environments.")

st.markdown("- Analyze gesture, encryption, and network patterns for risk indicators.")

st.markdown("- Visualize system performance and threat events interactively.")
      
st.markdown("- Visualize system performance and threat events interactively.")

st.markdown("- Detect anomalies using outlier analysis and statistical methods.")

st.markdown("- Propose data-driven security strategies to mitigate threats.")

st.subheader("📊 Dataset Highlights:")
st.text("The dataset contains 1,000 entries and 18 attributes, capturing telemetry and cybersecurity aspects of telesurgery:")
st.markdown("- **Gesture Data**: Type, duration, and 3D coordinates of robot movements.")
st.markdown("- **Communication Info**: Sender/receiver roles, encryption algorithm used, and encryption status.")
st.markdown("- **Network Metrics**: Latency, data transfer rate.")
st.markdown("- **Threat Metadata**: Type, severity, whether detected, and response actions taken.")

st.subheader("🔍 Key Analyses Performed:")
st.markdown("- **Gesture Efficiency**: Analyze performance across different gesture types and durations.")
st.markdown("- **Threat Mapping**: Identify which actions or network states are most associated with security risks.")
st.markdown("- **Network Health**: Evaluate how latency and bandwidth affect cybersecurity.")   
st.markdown("- **Response Effectiveness**: Assess timeliness and adequacy of threat mitigation strategies.") 
st.markdown("- **Encryption Security**: Compare success/failure rates of encryption algorithms under different conditions.")

st.subheader("🔢 Numerical Features")
st.markdown("🔢 **Numerical Features**")
st.markdown("-Gesture Duration (sec)")
st.markdown("- Network Latency (ms)")
st.markdown("- Data Transfer Rate (Mbps)")
st.markdown("- Response Time (sec)")
st.markdown("- Threat Detected (binary: 0 or 1)")

st.markdown("**Key observations:**")
st.markdown("- Gesture durations ranged from quick movements (~1 sec) to extended procedures (>5 sec).")
st.markdown("- Latency values were mostly under 20 ms, but occasional spikes suggest potential lag-related vulnerabilities.")
st.markdown("- Transfer rates varied widely, indicating fluctuating bandwidth during surgery.")
st.markdown("- Some response times were unexpectedly long for high-severity threats, hinting at gaps in response protocols.")

st.subheader("🧮 Categorical Features")
st.markdown("**These include:**")
st.markdown("- Gesture Type (e.g., Incision, Suturing)")
st.markdown("- Robot Status (Active, Idle)")
st.markdown("- Sender / Receiver (Operator ↔ Robot)")
st.markdown("- Encryption Algorithm Used (e.g., Two Fish)")
st.markdown("- Encryption Status (Encrypted, Failed)")
st.markdown("- Threat Type and Threat Severity")

st.markdown("**Findings:**")
st.markdown("- “Incision” was the most frequent gesture type, followed by “Suturing.”")
st.markdown("- The majority of communications were encrypted, but a notable portion (~10%) had failed encryption.")
st.markdown("- “Man-in-the-Middle Attack” was the most common threat type, often tied to failed encryptions.")
st.markdown("- Low-severity threats were more frequent than high-severity ones, though some high-severity cases took longer to respond to.")









