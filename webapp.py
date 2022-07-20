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

@app.route("/view/<product_id>", methods=["GET", "POST"])
def view(product_id):
    if request.method == "GET":
        item=GUNDAM.find_item_by_id(product_id)
        return render_template("view.html", item=item), 200

    if request.method == "POST":
        search=request.form.get("search")
        return redirect(f"/search/{search}")



    
@app.route("/search/<search>", methods=["GET","POST"])
def search(search):
    if request.method == "GET":
        items=GUNDAM.find_items_by_id(search)
        if len(items) == 0:
            return "No Item Found", 404

        if len(items) == 1:
            return render_template("view.html", item=items[0]), 200
        
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