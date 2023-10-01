import time
import datetime
import knn

def dumb():
    pass

class datapoint(object):
    def __init__(self, url, timestamp: str, title: str):
        self.url = url
        self.timestamp = self.time_calculation(timestamp)
        self.timestamp_int = timestamp
        self.title = title
        self.day_of_week = self.day_of_week_calculation(self.timestamp)
        self.productivity = self.productivity_calculation(self.url, self.title)
        self.toKNN = self.represent_for_Knn
        
    def time_calculation(self, timestamp) ->datetime.datetime:
        try:
            t = datetime.datetime.fromtimestamp(int(float(timestamp)))
            return t
        except OSError:
            print(timestamp)
            
    # Returns an a float between 0 and 1, where 1 is defined as productive according to url and title
    # Kenneth
    def productivity_calculation(self, url, title)-> float:
        # word2vec
        return 1
    
    def day_of_week_calculation(self,timestamp):
        timestamp = datetime.datetime.date(timestamp)
        day = timestamp.weekday()
        return day
    
    def represent_for_Knn(self):
        return [self.day_of_week, self.timestamp_int, self.productivity]
    
    def __repr__(self):
        return f"url:{self.url}\nint timestamp:{self.timestamp_int}\nTitle:{self.title}\nDay of Week:{self.day_of_week}\nProductivity:{self.productivity}"



'''
a = datapoint("abc/abs.com", "24234324234.082", "abs.com")
print(a)
'''
    
        
    
    
    