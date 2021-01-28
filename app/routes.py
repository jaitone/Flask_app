from flask import Flask
from flask import jsonify, request, json

from app.models.movies_model import Film
from app import app

import os


@app.route('/')

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/movies', methods=['GET'])
def get_all_movies():
    all_movies = Film.get_all_films()
    return jsonify(
        movies = [movie.films_serializer for movie in all_movies]
        )

@app.route("/submit_film", methods=["POST"])
def submit_film():
    incoming = request.get_json()

    print(incoming, "hello incoming")
    success, id = Film.save(Film (
        incoming["film_name"],
        incoming["img_url"],
        incoming["release_year"],
        incoming["summary"],
        incoming["director"],
        incoming["genre"],
        incoming["rating"],
        incoming["film_runtime"],
        incoming["meta_score"]
        ))

    if not success:
        return jsonify(message="Error submitting film", id=None), 409

    return jsonify(success=True, id=id)

@app.route("/delete_film/<int:film_id>", methods=["DELETE", "POST"])
def delete_film(film_id):
    success = Film.delete(film_id)
    if not success:
        return jsonify(message="Error deleting film"), 409

    return jsonify(success=True)


# @app.route("/api/edit_film", methods=["POST"])
# @requires_auth
# def edit_film():
#     incoming = request.get_json()
   
#     success = film.edit_film(
#         incoming.get('film_id'),
#         incoming.get('film'),
#         incoming.get('status')
#     )
#     if not success:
#         return jsonify(message="Error editing film"), 409

#     return jsonify(success=True)