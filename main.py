from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SECRET_KEY"] = "gvsyuagfjhcsgzhjgvcjhsgjdzfd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)
class Store(db.Model):
     item = db.Column(db.Integer, primary_key=True)
     number = db.Column(db.Integer)
     buyingPrice = db.Column(db.Float)

class Sold(db.Model):
    item = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    sellingPrice = db.Column(db.Float)
    date = db.Column(db.DateTime)



class SELL:
    def seller(self, item, number, sellingPrice):
        self.item = item
        self.number = number
        self.sellingPrice = sellingPrice
        store = Store()
        date = datetime.today()
        query = store(item=item, number=number, sellingPrice=sellingPrice, date=date.strftime("d%-m%-y%"))
        return "Item sold!!"

    def manager(self):
        data = Store.query.all()
        return data

    def storage(self, item, number, buyingPrice):
        self.item = item
        self.number = number
        self.buyingPrice = buyingPrice
        store = Store()
        query = store(item=item, number=number, BuyingPrice=buyingPrice)

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/", methods=["GET", "POST"])
def selling():
    if request.method == "POST":
        item = request.form["number"]
        number = request.form["item"]
        sellingPrice = request.form["sellingPrice"]
        return redirect(url_for("selling"), 304, Response="NOt Modified")
    return render_template("selling.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email2"]
        password = request.form["password2"]
    return render_template("login.html")

@app.route("/view")
def view():
    return "hello"


@app.route("/stock")
def stoke():
    return "hello"





if __name__ == "__main__":
    app.run(debug=True)

