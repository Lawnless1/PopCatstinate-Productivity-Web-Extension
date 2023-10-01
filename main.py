from process import processBrowserHistory
from flask import Flask

app = Flask(__name__)

@app.route("/lol", methods = ["GET"])
def lol():
    return "rip bozo"


@app.route("/process", methods = ["GET"])
def processHistory():
    return processBrowserHistory("{\"a\":1}")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080)