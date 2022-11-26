import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
#link do bazy danych
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#tworzenie bazy danych
db = SQLAlchemy(app)

# typ bazy danych
# PROJEKT - klasa modelu, atrybuty:
#nazwa
#kategoria
#link
#created_at
#czy ukończono

class Project(db.Model): #model - baza danych, zapisywanie, usuwanie
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) #typ bazy danych, string max 100 znaków nie może być pusty
    category = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    finished = db.Column(db.Boolean)

    def __repr__(self): #funkcja reprezentacyjna
        return f'<Project {self.title}>' #self.x -konkretny obiekt


@app.route("/") #dekorator, przekirowanie - główny adres
def hello_world():
    return render_template("index.html")