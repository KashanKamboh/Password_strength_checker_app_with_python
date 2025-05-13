# 🔐 Password Strength Checker

A simple and interactive **Password Strength Checker** built with Python and Streamlit. This app helps users evaluate how strong their passwords are and encourages the use of secure practices by giving real-time feedback.

## 🚀 Features

- **Real-Time Strength Detection**: Evaluates password strength based on five criteria:
  - Minimum length
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters

- **Visual Feedback**: Displays strength using:
  - Emojis and labels (e.g., Weak ❌😬, Moderate 😐💭, Strong ✅💪)
  - A progress bar
  - Color-coded messages (red, orange, green)

- **Responsive UI**: Styled using custom CSS for a clean, modern look with a light blue background and navy text.

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – For the interactive web UI
- **Regular Expressions (re)** – For pattern matching in passwords

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install streamlit pandas
Run the app:

bash
Copy
Edit
streamlit run passward_strenght_meter.py

📊 Scoring Criteria
Condition	Points
Password length > 0	1
Contains lowercase letter [a-z]	1
Contains uppercase letter [A-Z]	1
Contains digit [0-9]	1
Contains special character	1

Max Score: 5

📷 Screenshot
Add a screenshot here of your app running
(Use: streamlit run > open in browser > take screenshot)
