# TODO: Feature 1
#test_get_all_movies.py
from src.repositories.movie_repository import get_movie_repository

def test_get_all_movies():
    movies = get_movie_repository()
    movies.create_movie('Movie', 'Guy', 3)
    assert len(movies.get_all_movies()) == 2
    movies.create_movie('Another', 'Person', 4)
    assert len(movies.get_all_movies()) == 3
    
