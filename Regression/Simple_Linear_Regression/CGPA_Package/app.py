import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd

# Load trained model
with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 CGPA vs Salary Prediction")
st.write("This app predicts **Salary** based on **CGPA** using Linear Regression.")

# User input
cgpa = st.number_input("Enter your CGPA:", min_value=0.0,
                       max_value=10.0, value=5.0, step=0.1)

# Predict salary
if st.button("Predict Salary"):
    prediction = model.predict(np.array([[cgpa]]))[0]   # take scalar
    st.success(f"Predicted Salary: ${prediction}k")

    # Prepare regression line
    X_range = np.linspace(0, 10, 100).reshape(-1, 1)  # CGPA from 0 to 10
    Y_pred = model.predict(X_range)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(X_range, Y_pred, color="red", label="Regression Line")
    ax.scatter(cgpa, prediction, color="green", s=100,
               marker="x", label="Your Prediction")

    ax.set_xlabel("CGPA")
    ax.set_ylabel("Salary ($1000s)")
    ax.set_title("CGPA vs Salary Prediction")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
