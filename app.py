from flask import Flask, render_template, request
import re

app = Flask(__name__)

COMMON_PASSWORDS = {"123456", "password", "123456789", "12345678", "qwerty", "abc123", "password1"}

def evaluate_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Use both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Include at least one special character (e.g., @, #, $).")

    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid using common passwords.")
        score = min(score, 2)

    if score >= 5:
        strength = "Strong 💪"
        color = "success"
    elif score >= 3:
        strength = "Moderate 🛡️"
        color = "warning"
    else:
        strength = "Weak ⚠️"
        color = "danger"

    return strength, color, suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    color = None
    suggestions = []

    if request.method == 'POST':
        password = request.form['password']
        strength, color, suggestions = evaluate_password(password)

    return render_template('index.html', strength=strength, color=color, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
