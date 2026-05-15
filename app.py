from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
import random

from dotenv import load_dotenv
import os

load_dotenv()

from questions import questions
from database import init_db, insert_result, get_results, get_attempt_count

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# ---------------- MAIL CONFIG ----------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

init_db()

user_data = {}

# ---------------- LOGIN ----------------
@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']

        otp = str(random.randint(100000, 999999))
        user_data[email] = {"otp": otp}

        msg = Message("OTP Verification", recipients=[email])
        msg.body = f"Your OTP is {otp}"
        mail.send(msg)

        session['email'] = email

        return redirect(url_for("verify"))

    return render_template("login.html")


# ---------------- VERIFY ----------------
@app.route('/verify', methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        email = session.get("email")
        otp_entered = request.form['otp']

        if email and otp_entered == user_data[email]["otp"]:
            return redirect(url_for("home"))
        else:
            return "Invalid OTP ❌"

    return render_template("verify.html")


# ---------------- QUIZ ----------------
@app.route('/quiz')
def home():
    email = session.get("email")

    if not email:
        return redirect(url_for("login"))

    attempt_count = get_attempt_count(email)

    return render_template(
        'quiz.html',
        questions=questions,
        attempt=attempt_count + 1
    )


# ---------------- SUBMIT ----------------
@app.route('/submit', methods=['POST'])
def submit():
    email = session.get("email")

    if not email:
        return redirect(url_for("login"))

    score = 0

    for i, q in enumerate(questions):
        user_ans = request.form.get(f"q{i+1}")
        if user_ans == q["answer"]:
            score += 1

    total = len(questions)

    insert_result(email, score, total)

    results = get_results(email)

    return render_template(
        'result.html',
        score=score,
        total=total,
        results=results
    )


# ---------------- HISTORY ----------------
@app.route('/history')
def history():
    email = session.get("email")

    if not email:
        return redirect(url_for("login"))

    data = get_results(email)

    return render_template('history.html', results=data)


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)