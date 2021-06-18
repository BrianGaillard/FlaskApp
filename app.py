from flask import Flask, render_template
from funny_rank import FunnyRankings



app = Flask(__name__)

@app.route("/")
def homepage():
    rankings = FunnyRankings()


    return render_template("layout.html", rankings = rankings)

if __name__ == '__main__':
    app.run(debug=True)
