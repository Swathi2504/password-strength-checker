from flask import Flask, render_template, request
import re

app = Flask(__name__)

common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "welcome",
    "password123"
]

def analyze_password(password):

    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    # Number Check
    if re.search(r"\d", password):
        score += 15
    else:
        suggestions.append("Add numbers")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        suggestions.append("Add special characters")

    # Common Password Detection
    common = False

    if password.lower() in common_passwords:
        common = True
        score -= 20
        suggestions.append("This is a commonly used password")

    # Repeated Characters Detection
    if re.search(r"(.)\1{2,}", password):
        score -= 10
        suggestions.append(
            "Avoid repeated characters (e.g., aaa, 111)"
        )

    # Sequential Pattern Detection
    sequences = [
        "123", "234", "345", "456", "567", "678", "789",
        "abc", "bcd", "cde", "def",
        "qwerty"
    ]

    for seq in sequences:
        if seq in password.lower():
            score -= 10
            suggestions.append(
                "Avoid predictable sequences"
            )
            break

    # Prevent Negative Scores
    score = max(score, 0)

    # Limit Maximum Score
    score = min(score, 100)

    # Strength Classification
    if score < 40:
        strength = "Weak"
        color = "danger"

    elif score < 80:
        strength = "Medium"
        color = "warning"

    else:
        strength = "Strong"
        color = "success"

    return (
        score,
        strength,
        color,
        suggestions,
        common
    )

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        password = request.form["password"]

        (
            score,
            strength,
            color,
            suggestions,
            common
        ) = analyze_password(password)

        result = {
            "score": score,
            "strength": strength,
            "color": color,
            "suggestions": suggestions,
            "common": common,
            "length": len(password),

            # Security Checklist
            "has_upper": bool(
                re.search(r"[A-Z]", password)
            ),

            "has_lower": bool(
                re.search(r"[a-z]", password)
            ),

            "has_digit": bool(
                re.search(r"\d", password)
            ),

            "has_special": bool(
                re.search(
                    r"[!@#$%^&*(),.?\":{}|<>]",
                    password
                )
            ),

            "has_length": len(password) >= 8
        }

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)