from flask import Blueprint, request, jsonify
from app.models import db, Order, OrderItem, Menu

order_controller = Blueprint('order_controller', __name__)

@order_controller.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    items = data.get('items')  # List of menu items with quantities
    
    new_order = Order(user_id=user_id)
    db.session.add(new_order)
    db.session.commit()
    
    for item in items:
        menu_item = Menu.query.get(item['menu_id'])
        if menu_item:
            order_item = OrderItem(order_id=new_order.id, menu_id=menu_item.id, quantity=item['quantity'])
            db.session.add(order_item)
    
    db.session.commit()
    
    return jsonify({"message": "Order created successfully"}), 201
