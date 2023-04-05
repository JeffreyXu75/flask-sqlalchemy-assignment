from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# class Instructor(db.Model):
#     instructor_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255), nullable=False)
#     last_name = db.Column(db.String(255), nullable=False)
#     tenured = db.Column(db.Boolean, nullable=False)
# -- Create movie table
# CREATE TABLE movie (
#     movie_id SERIAL       NOT NULL,
#     title    VARCHAR(255) NOT NULL,
#     director VARCHAR(255) NOT NULL,
#     rating   INT NOT      NULL,
#     PRIMARY KEY (movie_id)
# );

class Movie(db.Model):
     movie_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(255), nullable=False)
     director = db.Column(db.String(255), nullable=False)
     rating = db.Column(db.Integer, nullable=False)

