from flask import Flask, render_template, request, url_for, redirect
#
# import getLyrics
# import analyzeLyrics

app = Flask(__name__)

artistSearched = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/searchArtist", methods=["POST", "GET"])
def searchArtist() :
    if request.method == "POST" :
        artistSearched = request.form["artistSearch"]
        return redirect(url_for("artist", search=artistSearched))
    else :
        return render_template("search.html")

    # return f"<p>Searched {name}: {analyzeLyrics.selfish_words / getLyrics.songCount} selfish words per song</p>"

@app.route("/<search>")
def artist(search):
    return f"<h1>{search}</h1>"


if __name__ == "__main__" :
    app.run(debug=True)
