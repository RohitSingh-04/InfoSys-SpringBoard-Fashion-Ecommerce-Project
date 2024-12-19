from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
db = SQLAlchemy()

#to be changed as per the ER Diagram Provided by the team
class User(UserMixin,db.Model):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    rating = db.Column(db.Float)
    ratting = db.Column(db.String(100))

    def __repr__(self):
        return f'<Product {self.name}>'
