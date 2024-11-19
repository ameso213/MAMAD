from flask import Blueprint, request, jsonify
from app.models import db, Gallery

gallery_controller = Blueprint('gallery_controller', __name__)

@gallery_controller.route('/gallery', methods=['GET'])
def get_gallery():
    images = Gallery.query.all()
    return jsonify([{'id': img.id, 'image_url': img.image_url, 'description': img.description} for img in images]), 200

@gallery_controller.route('/gallery', methods=['POST'])
def add_image():
    data = request.get_json()
    image_url = data.get('image_url')
    description = data.get('description')
    
    new_image = Gallery(image_url=image_url, description=description)
    db.session.add(new_image)
    db.session.commit()
    
    return jsonify({"message": "Image added to gallery"}), 201
