from knn import KNN
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datapt import datapoint 

f = open('data.json')
data = json.load(f)

master_list = []
for datapt in data["history"]:
    master_list.append(datapoint(datapt["url"], datapt["lastVisitTime"],datapt["title"]))

timestamp_int_to_datapoint = {} # Dictionary mapping timestamp int to datapoint class
for datapt in master_list:
    datapt: datapoint
    timestamp_int_to_datapoint[datapt.timestamp_int] = datapt

class Server(BaseHTTPRequestHandler):
    def process_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

# setup simple web server
hostName = "104.155.165.248"
serverPort = "8080"

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

    
    
