# 🔐 Password Strength Analyzer

A Python Flask-based web application that evaluates the strength of user passwords by analyzing common security factors such as length, uppercase letters, lowercase letters, numbers, special characters, and common password patterns.

This project was developed as part of the **Decode Labs Cybersecurity Internship**.

---

## 📌 Project Objective

The objective of this project is to help users create stronger and more secure passwords by:

- Checking password complexity
- Detecting weak passwords
- Providing security suggestions
- Displaying password strength visually

---

## ✨ Features

- ✅ Password length validation
- ✅ Uppercase letter detection
- ✅ Lowercase letter detection
- ✅ Number detection
- ✅ Special character detection
- ✅ Common password detection
- ✅ Password strength score
- ✅ Strength levels:
  - Weak
  - Medium
  - Strong
- ✅ Security improvement suggestions
- ✅ Responsive Bootstrap interface

---

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

---

## 📂 Project Structure

```
PasswordStrengthAnalyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/swathi2504/PasswordStrengthAnalyzer.git
```

### 2. Navigate to the project folder

```bash
cd PasswordStrengthAnalyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Password Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Length ≥ 8 | ✔ |
| Uppercase Letter | ✔ |
| Lowercase Letter | ✔ |
| Number | ✔ |
| Special Character | ✔ |
| Not a Common Password | ✔ |

---

## 💡 Example

**Input**

```
Password@123
```

**Output**

```
Strength: Strong
Score: 100%
Suggestions:
✔ Excellent password.
```

---


## 🔒 Security Concepts Used

- Password Complexity Analysis
- Basic Authentication Security
- Password Policy Enforcement
- Common Password Detection
- User Awareness

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Flask web development
- Password security principles
- Python string handling
- Regular expressions
- Frontend integration using Bootstrap
- Secure coding practices

---

## 🚀 Future Enhancements

- Password entropy calculation
- Password breach checking
- Password generator
- Dark mode
- Password visibility toggle
- Real-time strength meter
- Download security report

---

## 👩‍💻 Author

**Swathi L**


## 📄 License

This project is created for educational purposes as part of the Decode Labs Cybersecurity Internship.