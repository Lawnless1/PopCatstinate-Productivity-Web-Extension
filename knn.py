import random 
import numpy as np
from sklearn.neighbors import NearestNeighbors
from datapt import datapoint

def generate_random_data(N):
    # Generate random values for x (day of the week), y (time of the day), and z (productivity)
    x = np.random.randint(0, 7, N)  # Random integers between 0 and 6 (inclusive)
    
    # Generate random time values (hours and minutes)
    y_hours = np.random.randint(0, 24, N)  # Random hours between 0 and 23 (inclusive)
    y_minutes = np.random.randint(0, 60, N)  # Random minutes between 0 and 59 (inclusive)
    y = y_hours * 100 + y_minutes  # Combine hours and minutes to represent time
    
    z = np.random.randint(0, 2, N)  # Random integers (0 or 1) for productivity

    # Create the Data array with three dimensions
    Data = np.column_stack((x, y, z))

    return Data

'''==========================================================='''

def KNN(Data: list, Initial_Vector: list, K: int):
    
    
    # Create a dictionary to group data points by 'x' value
    x_to_data = {}
    for datapt in Data:
        datapt: datapoint
        point = datapt.toKNN
        x = point[0]
        if x in x_to_data:
            x_to_data[x].append(point)
        else:
            x_to_data[x] = [point]
    
    # Extract the attributes from the Initial_Vector
    x0, y0 = Initial_Vector[0], Initial_Vector[1]
    
    # Check if x0 exists in the data
    same_day = x_to_data[x0] if x0 in x_to_data else []
  
    # Extract the 'y' values from the same_day data points
    y_values = [point[1] for point in same_day]
    
    # Convert y_values to a NumPy array for scikit-learn
    y_values = np.array(y_values).reshape(-1, 1)

    if K > len(y_values):
        return {"point": {'x0': x0, 'y0': y0, 'prod_av': 0.5}, "neighbor":[]}
      # raise ValueError("K is larger than the number of available y_values")
  
    # Create a NearestNeighbors model
    nn_model = NearestNeighbors(n_neighbors=K)
    nn_model.fit(y_values)
    
    # Find the K nearest neighbors of y0
    distances, indices = nn_model.kneighbors([[y0]])
    
    # Extract the data points corresponding to the nearest neighbors
    neighbors = [same_day[i] for i in indices[0]]

    # print(neighbors)
  
    # Calculate the average 'z' value of the neighbors
    try:
        prod_av = np.mean([point[2] for point in neighbors])
    except Exception:
        prod_av = 0
    # Create the output data point
    output_point = {'x0': x0, 'y0': y0, 'prod_av': prod_av}
    
    return {"point": output_point, "neighbor":neighbors}


'''=====================================================

# Example usage:
N = 100  # You can specify the number of data points you want
data = generate_random_data(N)

print('data')
print(data)

Initial_Vector = np.array([3, 1600])

print('initial vector')
print(Initial_Vector)

K = 5 # Example K value

result = KNN(data, Initial_Vector, K)
print(result)
'''