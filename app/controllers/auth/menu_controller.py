from flask import Blueprint, request, jsonify
from app.models import db, Menu

menu_controller = Blueprint('menu_controller', __name__)

@menu_controller.route('/menu', methods=['GET'])
def get_menu():
    menu_items = Menu.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price} for item in menu_items]), 200

@menu_controller.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    
    new_item = Menu(name=name, description=description, price=price)
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify({"message": "Menu item added"}), 201
