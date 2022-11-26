from flask import Flask

app = Flask(__name__)

@app.route("/") #dekorator, przekirowanie - główny adres
def hello_world():
    return "<p>Hello, World!</p>"