from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello bala welcome to your code space!"