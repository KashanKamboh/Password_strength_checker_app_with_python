import streamlit as st
import pandas as pd
import re               #Regular expression library hai — yeh password ke andar letters, digits, special characters ko check karne ke kaam aati hai.

st.set_page_config(page_title="Password Strength Checker")
st.title("🔐 Password Strength Checker")

# Custom CSS for background, text colors and input box styling
st.markdown(
    """
    <style>
    /* Background and text colors for the app */
    .stApp {
        background-color: #add8e6;  /* light blue */
        color: navy;  /* navy blue text */
    }
    /* Style the text input box */
    input[type="password"], input[type="text"] {
        background-color: white !important;
         color: navy !important;
    }
    # /* Also style the placeholder text color */
    # ::placeholder {
    #     color:  navy !important;
    # }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("🚫💻 Protect Your Digital World with Strong Passwords: Check Your Password Strength Now 🚀")

password = st.text_input("Enter your password 🔒", type="password")

def password_strength(password):
    score = 0
    if len(password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[\d]" , password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # for checking if password weak, moderate or strong
    if score <= 2:
        return "Weak ❌😬" , score
    if score == 3:
        return "Moderate 😐💭" , score
    else :
        return "Strong Password ✅💪", score

if password:
    strength, score = password_strength(password)
    st.write(f"**Strength✨:** {strength}")
    
    # Visual Meter
    meter_colors = {
        "Weak ❌😬": "red",
        "Moderate 😐💭": "orange",
        "Strong Password ✅💪": "green"
    }

    st.progress(score / 5)
    st.markdown(
         f"<div style='color: {meter_colors[strength]}; font-weight: bold;'>Score: {score}/5 </div>",
        unsafe_allow_html=True)

