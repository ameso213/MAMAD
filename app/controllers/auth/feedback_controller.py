from flask import Blueprint, request, jsonify
from app.models import db, Feedback

feedback_controller = Blueprint('feedback_controller', __name__)

@feedback_controller.route('/feedback', methods=['POST'])
def give_feedback():
    data = request.get_json()
    user_id = data.get('user_id')
    order_id = data.get('order_id')
    rating = data.get('rating')
    comments = data.get('comments')
    
    new_feedback = Feedback(user_id=user_id, order_id=order_id, rating=rating, comments=comments)
    db.session.add(new_feedback)
    db.session.commit()
    
    return jsonify({"message": "Feedback submitted"}), 201
