from flask import (
    Blueprint, request, jsonify, session, render_template,
    redirect, url_for
)
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import random
import traceback

from . import db
from .models import User, Progress, MockProgress
from .utils import (
    generate_feedback,
    get_question_by_id,
    get_filtered_question,
    QUESTION_BANK
)

main = Blueprint('main', __name__)

UPLOAD_FOLDER = "app/static/uploads/photos"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# ---------------------------------------------
# HELPER
# ---------------------------------------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------
# SIGN UP / LOGIN
# ---------------------------------------------
@main.route("/sign", methods=["GET", "POST"])
def sign_page():
    if request.method == "POST":
        action = request.form.get("action")

        # -------- SIGNUP --------
        if action == "signup":
            first = request.form.get("first_name")
            last = request.form.get("last_name")
            email = request.form.get("email_signup")
            phone = request.form.get("phone_number")
            birthday = request.form.get("birthday")
            password = request.form.get("password_signup")
            confirm = request.form.get("confirm_password")

            if password != confirm:
                return render_template("sign.html", error="Passwords do not match")

            if User.query.filter_by(email=email).first():
                return render_template("sign.html", error="Email already exists!")

            user = User(
                first_name=first,
                last_name=last,
                email=email,
                phone_number=phone,
                birthday=birthday,
                password=generate_password_hash(password),
                streak=0,
                total_answers=0,
                points=0,
                last_answered=None
            )
            db.session.add(user)
            db.session.commit()

            session["user_id"] = user.id
            session["user_name"] = user.first_name

            return redirect(url_for("main.dashboard_page"))

        # -------- SIGNIN --------
        elif action == "signin":
            email = request.form.get("email_login")
            password = request.form.get("password_login")

            user = User.query.filter_by(email=email).first()
            if not user:
                return render_template("sign.html", error="Account does not exist")

            if not check_password_hash(user.password, password):
                return render_template("sign.html", error="Wrong password")

            session["user_id"] = user.id
            session["user_name"] = user.first_name
            session["user_photo"] = user.profile_photo

            return redirect(url_for("main.dashboard_page"))

    return render_template("sign.html")


@main.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.sign_page"))


# ---------------------------------------------
# BASIC PAGES
# ---------------------------------------------
@main.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("main.sign_page"))
    return redirect(url_for("main.dashboard_page"))


@main.route("/dashboard")
def dashboard_page():
    if "user_id" not in session:
        return redirect(url_for("main.sign_page"))
    return render_template("dashboard.html", user_id=session["user_id"])


@main.route("/interview")
def interview_page():
    if "user_id" not in session:
        return redirect(url_for("main.sign_page"))
    return render_template("interview_questions.html")


@main.route("/feedback")
def feedback_page():
    return render_template("feedback.html")


# ---------------------------------------------
# REVIEW (Practice Saved Answers)
# ---------------------------------------------
@main.route("/progress/<int:user_id>")
def progress_page(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template("review_responses.html", feedback_list=[])

    records = Progress.query.filter_by(user_id=user_id).order_by(Progress.timestamp.asc()).all()

    feedback_list = []
    for r in records:
        q = get_question_by_id(r.question_id)
        feedback_list.append({
            "question": q["question"] if q else "Unknown",
            "answer": r.answer,
            "feedback": r.feedback_text,
            "score": r.score,
            "sentiment": r.sentiment,
            "keywords": r.keywords,
            "time": r.timestamp.strftime("%Y-%m-%d %H:%M")
        })

    return render_template("review_responses.html", feedback_list=feedback_list)


# ---------------------------------------------
# GET CUSTOM QUESTION
# ---------------------------------------------
@main.route("/get_custom_question", methods=["POST"])
def get_custom_question_route():
    data = request.json

    q = get_filtered_question(
        data.get("company"),
        data.get("round_type"),
        data.get("difficulty")
    )

    if not q:
        return jsonify({"status": "error", "message": "No matching question"}), 404

    return jsonify({
        "status": "success",
        "question_id": q["id"],
        "question": q["question"],
        "keywords": q["keywords"]
    })


# ---------------------------------------------
# ANALYSE ANSWER
# ---------------------------------------------
@main.route("/analyse_answer", methods=["POST"])
def analyse_answer():
    data = request.json
    q = get_question_by_id(data["question_id"])

    result = generate_feedback(
        q["question"],
        data["answer"],
        q["keywords"],
        q.get("answer")
    )

    return jsonify({
        "status": "success",
        "keyword_score": result["keyword_score"],
        "sentiment_score": result["sentiment_score"],
        "final_feedback": result["final_feedback"]
    })


# ---------------------------------------------
# SAVE PRACTICE PROGRESS (FIXED)
# ---------------------------------------------
@main.route("/save_progress", methods=["POST"])
def save_progress():
    if "user_id" not in session:
        return jsonify({"status": "error", "message": "Not logged in"}), 401

    data = request.json
    user_id = session["user_id"]

    q = get_question_by_id(data["question_id"])
    if not q:
        return jsonify({"status": "error", "message": "Invalid question"}), 400

    result = generate_feedback(
        q["question"],
        data["answer"],
        q["keywords"],
        q.get("answer")
    )

    entry = Progress(
        user_id=user_id,
        question_id=data["question_id"],
        answer=data["answer"],
        feedback_text=result["final_feedback"],
        score=result["keyword_score"],
        sentiment=result["sentiment_score"],
        keywords=",".join(q["keywords"])
    )
    db.session.add(entry)

    # update user stats
    user = User.query.get(user_id)
    today = date.today().isoformat()

    if user.last_answered != today:
        user.streak = (user.streak or 0) + 1
        user.last_answered = today

    user.total_answers = (user.total_answers or 0) + 1
    user.points = (user.points or 0) + int(result["keyword_score"])

    db.session.commit()

    return jsonify({"status": "success"})


# ---------------------------------------------
# DASHBOARD DATA
# ---------------------------------------------
@main.route("/get_progress/<int:user_id>")
def get_progress_data(user_id):
    user = User.query.get(user_id)
    practice = Progress.query.filter_by(user_id=user_id).all()

    mock_count = MockProgress.query.filter_by(user_id=user_id).count()
    mock_interviews = mock_count // 10

    return jsonify({
        "status": "success",
        "streak": user.streak,
        "total_answers": user.total_answers,
        "points": user.points,
        "scores": [p.score for p in practice],
        "sentiment": [p.sentiment for p in practice],
        "keyword_counts": [len(p.keywords.split(",")) for p in practice],
        "mock_interview_count": mock_interviews
    })


# ---------------------------------------------
# MOCK INTERVIEW
# ---------------------------------------------
@main.route("/mock_interview")
def mock_interview_page():
    if "user_id" not in session:
        return redirect(url_for("main.sign_page"))

    questions = random.sample(QUESTION_BANK, 10)
    return render_template("mock_interview.html", questions=questions)


# ---------------------------------------------
# SAVE MOCK PROGRESS (FIXED + GROUPED)
# ---------------------------------------------
@main.route("/save_mock_progress", methods=["POST"])
def save_mock_progress():
    data = request.json
    user_id = session.get("user_id")

    # get last interview number
    last_num = db.session.query(db.func.max(MockProgress.interview_number)).filter_by(user_id=user_id).scalar()
    next_num = (last_num or 0) + 1

    for item in data:
        q = get_question_by_id(item["question_id"])
        result = generate_feedback(q["question"], item["answer"], q["keywords"], q.get("answer"))

        entry = MockProgress(
            user_id=user_id,
            question_id=item["question_id"],
            answer=item["answer"],
            feedback_text=result["final_feedback"],
            score=result["keyword_score"],
            sentiment=result["sentiment_score"],
            keywords=",".join(q["keywords"]),
            interview_number=next_num   # ⭐ IMPORTANT
        )
        db.session.add(entry)

    db.session.commit()
    return jsonify({"status": "success"})

# ---------------------------------------------
# MOCK REVIEW (FIXED GROUPING)
# ---------------------------------------------
@main.route("/mock_review/<int:user_id>")
def mock_review_page(user_id):
    records = (
        MockProgress.query.filter_by(user_id=user_id)
        .order_by(MockProgress.interview_number.asc(), MockProgress.timestamp.asc())
        .all()
    )

    groups = {}
    for r in records:
        if r.interview_number not in groups:
            groups[r.interview_number] = []

        q = get_question_by_id(r.question_id)

        groups[r.interview_number].append({
            "question": q["question"] if q else "Unknown",
            "answer": r.answer,
            "feedback": r.feedback_text,
            "score": r.score,
            "sentiment": r.sentiment,
            "keywords": r.keywords,
            "time": r.timestamp.strftime("%Y-%m-%d %H:%M")
        })

    return render_template("mock_review.html", groups=groups)


# ---------------------------------------------
# PROFILE
# ---------------------------------------------
@main.route("/profile", methods=["GET", "POST"])
def profile_page():
    if "user_id" not in session:
        return redirect(url_for("main.sign_page"))

    user = User.query.get(session["user_id"])

    if request.method == "POST":
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.phone_number = request.form.get("phone_number")
        user.birthday = request.form.get("birthday")

        if "profile_photo" in request.files:
            photo = request.files["profile_photo"]
            if photo and allowed_file(photo.filename):
                filename = secure_filename(photo.filename)
                path = os.path.join(UPLOAD_FOLDER, filename)
                photo.save(path)
                user.profile_photo = filename
                session["user_photo"] = filename

        db.session.commit()
        return render_template("profile.html", user=user, success="Profile updated!")

    return render_template("profile.html", user=user)


# ---------------------------------------------
# ONE-TIME FEEDBACK UPGRADE FIXED
# ---------------------------------------------
@main.route("/upgrade_feedback")
def upgrade_feedback():
    logs = []
    updated = 0

    try:
        rows = Progress.query.all()
        logs.append(f"Rows Found: {len(rows)}")

        for r in rows:
            q = get_question_by_id(r.question_id)
            if not q:
                logs.append(f"No question for row {r.id}")
                continue

            result = generate_feedback(
                q["question"],
                r.answer,
                q["keywords"],
                q.get("answer")
            )

            r.feedback_text = result["final_feedback"]
            r.score = result["keyword_score"]
            r.sentiment = result["sentiment_score"]
            r.keywords = ",".join(q["keywords"])

            updated += 1

        db.session.commit()
        logs.insert(0, f"Updated {updated} rows successfully.")

    except Exception as e:
        logs.append(str(e))
        logs.append(traceback.format_exc())

    return "<br>".join(logs)
