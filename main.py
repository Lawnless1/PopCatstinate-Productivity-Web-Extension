from process import processBrowserHistory
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route("/lol", methods = ["GET"])
def lol():
    return "rip bozo"


@app.route("/process", methods = ["GET"])
@cross_origin(supports_credentials=True)
def processHistory():
    return processBrowserHistory("{\"a\":1}")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080)