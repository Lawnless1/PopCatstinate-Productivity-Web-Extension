from knn import KNN
import json
from datapt import datapoint 

def processBrowserHistory():
  f = open('data.json')
  data = json.load(f)

  master_list = []
  for datapt in data["history"]:
      master_list.append(datapoint(datapt["url"], datapt["lastVisitTime"],datapt["title"]))

  timestamp_int_to_datapoint = {} # Dictionary mapping timestamp int to datapoint class
  for datapt in master_list:
      datapt: datapoint
      timestamp_int_to_datapoint[datapt.timestamp_int] = datapt

