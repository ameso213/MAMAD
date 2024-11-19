
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, completed, cancelled
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    payment = db.relationship('Payment', uselist=False, backref='order')
    order_items = db.relationship('OrderItem', backref='order', lazy=True)
