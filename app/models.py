from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    birthday = db.Column(db.String(20))
    streak = db.Column(db.Integer, default=0)
    total_answers = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)
    last_answered = db.Column(db.String,default=None)
    profile_photo = db.Column(db.String(200))

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.String(50))
    answer = db.Column(db.Text)
    feedback_text = db.Column(db.Text)
    keywords = db.Column(db.String(300))

    score = db.Column(db.Float, default=0.0)   # ⭐ FIXED
    sentiment = db.Column(db.Float, default=0.0)  # ⭐ FIXED

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class MockProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.String(50))
    answer = db.Column(db.Text)
    feedback_text = db.Column(db.Text)
    keywords = db.Column(db.String(300))

    score = db.Column(db.Float, default=0.0)  # ⭐ FIXED
    sentiment = db.Column(db.Float, default=0.0)  

    interview_number = db.Column(db.Integer)   # ⭐ REQUIRED for grouping mock interviews

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
