from piu import api_key
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/filme", methods=["GET"])
def home():
    title = genre = year = actors = director = rating = poster = error = ""
    movie = request.args.get("movie")
    if movie:
        url = f"http://www.omdbapi.com/?t={movie.lower()}&apikey={api_key}"
        search = requests.get(url)
        if search.status_code == 200:
            data = search.json()
            if data.get("Response") == "True":
                title = data["Title"]
                poster = data["Poster"]
                genre = data["Genre"]
                year = data["Year"]
                actors = data["Actors"]
                director = data["Director"]
                rating = data["imdbRating"]
            else:
                error = "Movie not found"
    else:
        error = "Request error"
    return render_template("index.html", movie=movie, title=title, genre=f"Genre:<br>{genre}", year=year, actors=f"Actors:<br>{actors}", director=f"Director:<br>{director}", rating=f"IMDB Rating:<br>{rating}", poster=poster, error=error)

if __name__ == "__main__":
    app.run(debug=True)