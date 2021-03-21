from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "bbe039da711aa33120ffe25823ae104d1daa0d8efc3e8b3ceb37a4819bf3f695"


@app.route("/", methods=['POST'])
def home():
    return render_template("home.html")


@app.route("/<query>", methods=['GET'])
def results(query):
    return render_template('results.html', title=query)


if __name__ == '__main__':
    app.run(debug=True)