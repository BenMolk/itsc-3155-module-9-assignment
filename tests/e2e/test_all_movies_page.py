# TODO: Feature 1
# test_all_movies_page.py
from flask.testing import FlaskClient
from app import movie_repository


def test_list_all_movies(test_app: FlaskClient):
    movie_repository.create_movie('Title', 'Director', 5)
    response = test_app.get('/movies')
    assert b'<td>Title</td>' in response.data
    assert b'<td>Director</td>' in response.data
    assert b'<td>5</td>' in response.data

