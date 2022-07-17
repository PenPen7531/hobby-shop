import collections
from flask import Flask, request, jsonify, render_template, redirect, session
from models.collection import Collection
app = Flask(__name__)
app.secret_key="Secretasdasdasdads"

GUNDAM=Collection("gundam")

@app.route("/", methods=["GET", "POST"])
def login():
    
    if request.method == "GET":
        print(GUNDAM)
        return render_template("home.html", collections=GUNDAM), 200

    if request.method == "POST":
        search=request.form.get("search")
        return redirect(f"/search/{search}")

@app.route("/view/<product_id>")
def view(product_id):
    item=GUNDAM.find_item_by_id(product_id)
    return render_template("view.html", item=item), 200

    
@app.route("/search/<search>", methods=["GET","POST"])
def search(search):
    if request.method == "GET":
        items=GUNDAM.find_items_by_id(search)
        for i in range(len(items)):
            print(items[i-1].name)
        return render_template("search.html", items=items), 200

    if request.method == "POST":
        search=request.form.get("search")
        return redirect(f"/search/{search}")


@app.route("/order/<product_id>")
def order(product_id):
    print(product_id)
    return "Tested"
if __name__ == "__main__":
    app.run(debug=True)