from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from funny_rank import FunnyRankings


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b2eb70701e05d178d1683604a5ca1ba9'


@app.route("/", methods=['GET', 'POST'])
def homepage():
    rankings = FunnyRankings()
    length = len(rankings)

    # use two diffferent buttons to toggle between sorting methods
    if request.method == 'POST':
        if request.form.get("submit_button") == 'High to Low':
                rankings.sort(reverse=True,key= lambda ranks : ranks[1])

                return render_template("layout.html", rankings = rankings, length = length)

        else:
                rankings.sort(reverse=False,key= lambda ranks : ranks[1])

                return render_template("layout.html", rankings = rankings, length = length)

    return render_template("layout.html", rankings = rankings, length = length)


if __name__ == '__main__':
    app.run(debug=True)
