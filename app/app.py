from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app: Flask = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/tesla"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = "feedback"

    id: int = db.Column(db.Integer, primary_key=True)
    customer: str = db.Column(db.String(200))
    dealer: str = db.Column(db.String(200))
    rating: int = db.Column(db.Integer)
    comments: str = db.Column(db.Text)

    def __init__(self, customer, dealer, rating, comments) -> None:
        super().__init__()
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        customer: str = request.form["customer"]
        dealer: str = request.form["dealer"]
        rating: int = request.form["rating"]
        comments: str = request.form["comments"]

        if request.form["customer"] == "" or request.form["dealer"] == "":
            return render_template("index.html", message="Campos obrigatorios não preenchidos")

        data: Feedback = Feedback(customer, dealer, rating, comments)
        db.session.add(data)
        db.session.commit()
        
        return render_template("success.html")

@app.route("/")
def index():
    return render_template('index.html')
