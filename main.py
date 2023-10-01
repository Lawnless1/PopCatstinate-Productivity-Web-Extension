from process import processBrowserHistory
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route("/lol", methods = ["GET"])
def lol():
    return "rip bozo"


@app.route("/process", methods = ["POST"])
@cross_origin(origins="*")
def processHistory():
    app.logger.info(request.json)
    content = processBrowserHistory(request.json)
    return content


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080, debug=True)