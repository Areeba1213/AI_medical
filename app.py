import streamlit as st
import json
import os
from predictor import Predictor
from user import User

USERS_FILE = "users.json"
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

st.set_page_config(page_title="AI Medical Predictor", layout="centered")

st.title(" AI Medical Predictor")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

users = load_users()
current_user = None

if choice == "Sign Up":
    st.subheader("Create Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if username in users:
            st.warning("User already exists.")
        else:
            users[username] = {"password": password}
            save_users(users)
            st.success("Account created! Please login.")

elif choice == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.success(f"Welcome, {username}")
            current_user = User(username)
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password.")

if st.session_state.get('logged_in'):
    st.subheader("Health Risk Checker")
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.number_input("Age", min_value=1, max_value=120)
    symptoms = st.multiselect("Select Symptoms", [
        "Lump", "Fatigue", "Weight Loss", "Headache", "Irregular Periods", "Chest Pain"
    ])

    if st.button("Analyze Risk"):
        pred = Predictor(gender, age, symptoms)
        result, confidence = pred.analyze()
        st.markdown(f"### 🩺 Potential Risk: {result}")
        st.markdown(f"**Confidence Level:** {confidence}%")

        if st.checkbox("💳 Get Full Report (Premium Feature)"):
            st.warning("This is a premium feature. Please upgrade to access detailed report.")

