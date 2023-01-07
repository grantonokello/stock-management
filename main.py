from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SECRET_KEY"] = "gvsyuagfjhcsgzhjgvcjhsgjdzfd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
class Store(db.Model):
     id = db.Column(db.Integer, primary_key=True, unique=True)
     item = db.Column(db.Integer)
     number = db.Column(db.Integer)
     buyingPrice = db.Column(db.Float)

     def __init__(self, id, item, number, buyingPrice):
         self.id =id
         self.item = item
         self.number =number
         self.buyingPrice = buyingPrice


class Sold(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    item = db.Column(db.Integer)
    number = db.Column(db.Integer)
    sellingPrice = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __int__(self, item, number, sellingPrice, date):
        self.item = item
        self.number = number
        self.sellingPrice = sellingPrice
        self.date = date



class SELL:
    def seller(self, item, number, sellingPrice):
        self.item = item
        self.number = number
        self.sellingPrice = sellingPrice
        date = datetime.today()
        store = Store()
        query = store(item=item, number=number, sellingPrice=sellingPrice, date=date.strftime("d%-m%-y%"))

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

@app.route("/selling", methods=["GET", "POST"])
def selling():
    if request.method == "POST":
        item = request.form["number"]
        number = request.form["item"]
        sellingPrice = request.form["sellingPrice"]
        date = datetime.today()
        data = Sold()
        sell = data(item = item, number = number, sellingPrice = sellingPrice, date=date.strftime("d%-m%-y%"))
        db.session.add(sell)
        db.session.commit()
        flash("item sold")
        return redirect(url_for("selling"), 304, Response="NOt Modified")
    return render_template("selling.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["email2"]
        password = request.form["password2"]
        if name == "culture united" and password == "123456789":
            return redirect(url_for("view"))
    return render_template("login.html")

@app.route("/view")
def view():
    return render_template("view.html")


@app.route("/")
def stoke():
    return render_template("stock.html")





if __name__ == "__main__":
    app.run(debug=True)

