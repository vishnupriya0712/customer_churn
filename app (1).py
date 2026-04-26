import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("📊 Text Classification (ML Model)")

st.write("Enter numerical features manually:")

# ⚠️ Replace number of inputs based on your dataset
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")
feature4 = st.number_input("Feature 4")
feature5 = st.number_input("Feature 5")

if st.button("Predict"):

    data = np.array([[feature1, feature2, feature3, feature4, feature5]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Class 1")
    else:
        st.error("Class 0")
