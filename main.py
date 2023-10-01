from process import processBrowserHistory
from flask import Flask

app = Flask(__name__)

@app.route("/process")
def processHistory():
    processBrowserHistory()
    return "TEST"