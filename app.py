from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #dekorator, przekirowanie - główny adres
def hello_world():
    return render_template("index.html")