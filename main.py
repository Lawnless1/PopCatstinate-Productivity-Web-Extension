from process import processBrowserHistory
from flask import Flask

app = Flask(__name__)

@app.route("/process", methods = ["POST"])
def processHistory():
    # request.form?
    processBrowserHistory()
    return "{}"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080)