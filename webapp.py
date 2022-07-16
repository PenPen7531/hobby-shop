from flask import Flask, request, jsonify, render_template, redirect, session
from models.collection import Collection
app = Flask(__name__)
app.secret_key="Secretasdasdasdads"


@app.route("/", methods=["GET", "POST"])
def login():
    gundam=Collection("gundam")
    if request.method == "GET":
        return render_template("home.html", collections=gundam), 200



if __name__ == "__main__":
    app.run(debug=True)