from flask import Flask, render_template, url_for, request
from toipa import shentoipa

app = Flask(__name__)


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


@app.route("/", methods=["GET"])
def search():
    hanterm = str(request.values.get("term"))
    print(hanterm)
    if request.method == "GET" and hanterm != "None":
        d[hanterm]["ipa"] = shentoipa(d[hanterm]["pin"])
        return render_template(
            "results.html",
            title=hanterm,
            postdata=d[hanterm],
        )
    return render_template("index.html", title="Search")


if __name__ == '__main__':
    app.run(debug=True)
