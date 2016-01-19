from flask import Flask, request, render_template, redirect
from jinja2 import Template
app = Flask(__name__)

items = [] # list of objects with a "text" attribute

@app.route("/", methods=["GET"])
def show_items():
    return render_template("items.html", items=items)

@app.route("/create", methods=["POST"])
def create_item():
    pass

@app.route("/delete", methods=["POST"])
def delete_item():
    pass

if __name__ == "__main__":
    app.run(debug=True)
