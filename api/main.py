from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

parser = reqparse.RequestParser()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.year}', '{self.genre}')"
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'genre': self.genre
        }
    
    def serialize_short(self):
        return {
            'id': self.id,
            'title': self.title
        }
    
    def __str__(self) -> str:
        return super().__str__()
    

with app.app_context():
    db.create_all()