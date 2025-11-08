import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("cleaned_dataset.csv")

st.title("Exploratory Data Analysis of Telesurgery Cybersecurity Dataset")

st.text("The data exploration phase is essential to understanding the structure, trends, and potential quality issues in the dataset. For this project, we conducted an in-depth exploratory data analysis (EDA) on the Cybersecurity Threat Detection in 5G Telesurgery Systems dataset. The goal was to uncover patterns related to robotic gestures, network behavior, encryption performance, and threat indicators")


tab1, tab2 = st.tabs(["EDA 1","EDA 2"])

with tab1:
    st.subheader("1.Gesture Frequency")
    fig1 = px.histogram(df, x='Gesture_Type')
    st.plotly_chart(fig1)

    st.subheader("2.Average Gesture Duration per Type")   
    fig2 = px.box(df, x='Gesture_Type', y='Gesture_Duration_(sec)')
    st.plotly_chart(fig2)

    st.subheader("3.Gesture Duration vs. Response Time (sec)")
    fig3 = px.histogram(df, x='Response_Time_(sec)', y='Gesture_Duration_(sec)', color='Robot_Status',barmode='group')
    st.plotly_chart(fig3)

    st.subheader("4.Latency vs. Threat Detected")
    fig4 = px.scatter(df, x='Network_Latency_(ms)', y='Data_Transfer_Rate_(Mbps)',
                 color='Threat_Detected')
    fig4.update_layout(width=1000,height=600)
    st.plotly_chart(fig4)

    st.subheader("5.Encryption Algorithm Usage")
    fig5 = px.pie(df, names='Encryption_Algorithm_Used')
    st.plotly_chart(fig5)

with tab2:
    st.subheader("6.Threat Type Frequency")
    fig6 = px.histogram(df, x='Threat_Type')
    st.plotly_chart(fig6)

    st.subheader("7.Threat Severity vs. Response Time")
    fig7 = px.violin(df, y='Response_Time_(sec)', x='Threat_Severity',
                box=True, points='all')
    st.plotly_chart(fig7)

    st.subheader("8.Response Actions Taken")
    fig8 = px.histogram(df, x='Response_Action_Taken')
    st.plotly_chart(fig8)

    st.subheader("9.Threat Detected by Gesture Type")
    fig9 = px.sunburst(df, path=['Gesture_Type', 'Threat_Type'])
    fig9.update_layout(width=1000,height=500)
    st.plotly_chart(fig9)

    st.subheader("10. Gesture Coordinates")
    coords = df['Gesture_Coordinates_(x, y, z)'].str.extract(r'\((.*), (.*), (.*)\)')
    df[['x', 'y', 'z']] = coords.astype(float)

    fig10 = px.scatter_3d(df, x='x', y='y', z='z',
                    color='Gesture_Type')
    fig10.update_layout(width=1000,height=600)
    st.plotly_chart(fig10)

st.markdown("""
---  
### 🧾 **Conclusion**

This analysis provided a thorough overview of the **Telesurgery Cybersecurity Dataset**, beginning with essential preprocessing steps such as renaming all columns for consistency, handling missing values in key fields, and removing non-informative attributes like timestamps.

By applying clear and structured data cleaning techniques, we ensured the dataset is both accurate and easier to interpret. The visual exploration that followed helped uncover important patterns in the data — highlighting the distribution of key features, identifying potential irregularities, and offering early insights into the operational and security-related aspects captured within the dataset.

These foundational steps not only improve the dataset’s quality but also enhance our understanding of the underlying structure and behavior of the data. This positions us to conduct more focused, informed, and reliable analyses in the next stages of the project.
""")




