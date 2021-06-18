from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField
from funny_rank import FunnyRankings

class ButtonForm(FlaskForm):
    submit = SubmitField('Change Rank Order')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b2eb70701e05d178d1683604a5ca1ba9'

@app.route("/", methods=['GET', 'POST'])
def homepage():
    rankings = FunnyRankings()
    length = len(rankings)
    form = ButtonForm()
    flipbool = True
    rankings.sort(reverse=flipbool,key= lambda ranks : ranks[1])

    if form.validate_on_submit():
            rankings.sort(reverse=(~flipbool),key= lambda ranks : ranks[1])
            return render_template("layout.html", rankings = rankings, length = length, form=form)


    return render_template("layout.html", rankings = rankings, length = length, form=form)

if __name__ == '__main__':
    app.run(debug=True)
