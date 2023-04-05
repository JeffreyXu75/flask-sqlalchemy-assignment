from src.models import Movie, db
from sqlalchemy import func
class MovieRepository:
    

    def get_all_movies(self):
        # TODO get all movies from the DB
        all = Movie.query.all()
        return all

    def get_movie_by_id(self, movie_id2):
        # TODO get a single movie from the DB using the ID
        x = Movie.query.filter_by(movie_id=movie_id2).first()
        return x

    def create_movie(self, title2, director2, rating2):
        # TODO create a new movie in the DB
        new_movie = Movie(title=title2, director=director2, rating=rating2)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        x = Movie.query.filter((func.lower(Movie.title).like('%'+title.lower()+'%'))).all()
        return x


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
