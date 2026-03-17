from flask import Flask, render_template
from db import init_db, read_notes


app = Flask(__name__)


@app.route("/")
def home():
    notes = read_notes()
    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
