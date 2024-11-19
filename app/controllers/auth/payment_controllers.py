from flask import Blueprint, request, jsonify
from app.models import db, Payment, Order

payment_controller = Blueprint('payment_controller', __name__)

@payment_controller.route('/payment', methods=['POST'])
def make_payment():
    data = request.get_json()
    order_id = data.get('order_id')
    amount = data.get('amount')
    payment_method = data.get('payment_method')
    
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"message": "Order not found"}), 404
    
    new_payment = Payment(order_id=order.id, amount=amount, payment_method=payment_method)
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({"message": "Payment successful"}), 201
