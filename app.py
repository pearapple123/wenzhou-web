from flask import Flask, render_template, url_for, request, redirect, session
from form import SearchForm
import json
from flask_session import Session
# from toipa import shentoipa

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)
app.config['SECRET_KEY'] = "bbe039da711aa33120ffe25823ae104d1daa0d8efc3e8b3ceb37a4819bf3f695"

with open("sample.json", "r", encoding="utf-8") as f:
    jsond = f.read()
d = json.loads(jsond)


@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.is_submitted():
        session['hanterm'] = request.form.get("term")
        return redirect("results.html")
    return render_template("index.html", title="Search", form=form)


@app.route("/result")
def results():
    getdata = str(session.get("hanterm", None))
    print("Getdata is " + getdata)
    postdata = d[getdata]
    return render_template("results.html", title=getdata, postdata=postdata)


if __name__ == '__main__':
    app.run(debug=True)
