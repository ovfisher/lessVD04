from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    return render_template("ex4.html")


@app.route("/person/")
def person():
    return render_template("ex4_4.html")


if __name__ == "__main__":
    app.run()