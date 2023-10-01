from knn import KNN
import ujson as json
from datapt import datapoint 

def processBrowserHistory(f):
    data = json.loads(f)
    print("dsfyauiyfuisdfysudifyasdufu")
    print(data)
    return "{\"a\":1}"
    '''
    master_list = []
    for datapt in data["history"]:
        master_list.append(datapoint(datapt["url"], datapt["lastVisitTime"],datapt["title"]))

    timestamp_int_to_datapoint = {} # Dictionary mapping timestamp int to datapoint class
    for datapt in master_list:
        datapt: datapoint
        timestamp_int_to_datapoint[datapt.timestamp_int] = datapt
    extra_time = 0
    output = {"websites": [], "weeks":[]}
    for week in range(4):
        days = []
        extra_time += 604800
        for day_of_week in range(7):
            ls2 = []
            hours = []
            extra_time += 86400
            for time in range(24):
                extra_time += 3600
                k_neighbors = KNN(master_list, [day_of_week, 1693540801], 2)
                vector = k_neighbors["point"]
                neighbors = k_neighbors["neighbor"]
                ls2.append(vector[2])
                urls = [timestamp_int_to_datapoint[neigh[1]].url for neigh in neighbors]
                for url in urls:
                    output["websites"].append(url)
                hours.append({"averageProductivity": vector[2], "websites": urls})
            average_productivity = round(sum(ls2)/24, 2)
            days.append({"averageProductivity": average_productivity, "hours": hours})
            output["weeks"].append({"days": days})
    y = json.dumps(output)
    return y

'''