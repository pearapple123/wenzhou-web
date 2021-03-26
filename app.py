from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "bbe039da711aa33120ffe25823ae104d1daa0d8efc3e8b3ceb37a4819bf3f695"


class SearchForm(FlaskForm):
    term = StringField(label=('Search for:'), validators=[DataRequired()])
    submit = SubmitField(label=('Search'))


d = {
    "我": {
        "eng": "I, me",
        "pin": "ng4"
    },
    "你": {
        "eng": "you",
        "pin": "nyi4"
    }
}


@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "POST":
        print(form.term.data)
        hanterm = form.term.data
        postdata = d[hanterm]
        return render_template("results.html", title=hanterm, postdata=postdata)
    return render_template("index.html", title="Search", form=form)


if __name__ == '__main__':
    app.run(debug=True)
