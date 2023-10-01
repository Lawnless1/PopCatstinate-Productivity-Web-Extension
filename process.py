from knn import KNN
import json
from datapt import datapoint 
import tldextract

def processBrowserHistory(f):
    data = f
    # with open('data2.json', 'r', encoding="utf8") as f:
        # data = json.load(f)
    master_list = []
    for datapt in data:
        master_list.append(datapoint(datapt["url"], datapt["lastVisitTime"],datapt["title"]))

    timestamp_int_to_datapoint = {} # Dictionary mapping timestamp int to datapoint class
    for datapt in master_list:
        datapt: datapoint
        timestamp_int_to_datapoint[datapt.timestamp_int] = datapt
    extra_time = 0
    output = {"websites": [], "weeks":[]}
    ib = 0
    for week in range(4):
        ib += 1
        days = []
        extra_time += 604800
        for day_of_week in range(7):
            ls2 = []
            hours = []
            extra_time += 86400
            for time in range(24):
                extra_time += 3600
                k_neighbors = KNN(master_list[0:ib*(len(master_list)//2)], [day_of_week, 1696173462], 2)
                vector = k_neighbors["point"]
                neighbors = k_neighbors["neighbor"]
                vector = 0 if len(neighbors) == 0 else sum([float(i[2]) for i in neighbors])/len(neighbors)
                ls2.append(vector)
                urls = list(set([tldextract.extract(timestamp_int_to_datapoint[neigh[1]].url).domain.lower() for neigh in neighbors]))
                for url in urls:
                    output["websites"].append(tldextract.extract(url).domain.lower())
                hours.append({"averageProductivity": vector, "websites": urls})
            average_productivity = round(sum(ls2)/24, 2)
            days.append({"averageProductivity": average_productivity, "hours": hours})
            output["weeks"].append({"days": days})
    output["weeks"][::-1]
    output["websites"] = list(set(output["websites"]))
    y = json.dumps(output)
    return y
