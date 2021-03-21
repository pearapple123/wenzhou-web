from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/", methods=['POST'])
def home():
    return render_template("home.html")


@app.route("/<query>", methods=['GET'])
def result(query):
    return render_template('results.html', title=query)


if __name__ == '__main__':
    app.run(debug=True)