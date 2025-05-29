from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dogs.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(f"DB URI: {app.config['SQLALCHEMY_DATABASE_URI']}")  # Log for debugging

db = SQLAlchemy(app)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/rate', methods=['POST'])
def rate_dog():
    data = request.json
    new_rating = Rating(image_url=data['image_url'], rating=data['rating'])
    db.session.add(new_rating)
    db.session.commit()
    return jsonify({'message': 'Rating saved!'}), 201

@app.route('/ratings', methods=['GET'])
def get_ratings():
    ratings = Rating.query.all()
    return jsonify([{'id': r.id, 'image_url': r.image_url, 'rating': r.rating} for r in ratings])
