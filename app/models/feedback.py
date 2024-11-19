from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()




class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # rating out of 5
    comments = db.Column(db.String(255))
    feedback_date = db.Column(db.DateTime, default=datetime.utcnow)