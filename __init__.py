'''
Created on Sep 6, 2020

This program uses a set of data points and clusters them using the clustering algorithm. This also uses the elbow
method to find the most optimal k-value.

Various libraries like numPy, panda, sci-kit learn and matplot

@author: Sudesh Easwaran, freshman, Computer Engineering
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# reads the file with the numerical data to analyze
df = pd.read_csv("C:\\Users\\01sud\\Coding-Challenge\\ClusterPlot.csv")

# converts df to a numPy array
df.to_numpy()

#graphs the elbow graph showing the optimal k
distortionsArray = []
K_range = range(1,15) # range set at random but big enough to give an optimal k - value
for k in K_range:
    elbowModel = KMeans(n_clusters=k)
    elbowModel.fit(df)
    distortionsArray.append(elbowModel.inertia_)
    
plt.plot(K_range, distortionsArray, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show();

# to find a perfect k from the value that matches the graph
k = 0
arrayLength = len(distortionsArray)
i = 0
while i < arrayLength:
    old = distortionsArray[i]
    new = distortionsArray[i + 1]
    top = abs(new - old)
    # I set the threshold to a decrease less than 50%, 
    # as per many examples I had seen showed a  
    # trend of this instance to be the elbow or the most favorable k- value 
    if(top / old < .50):
        k= i + 1
        i = arrayLength
    else:
        i+= 1
    
# this creates clusters from the k-value found from the elbow method above
kmeans = KMeans(n_clusters = k)
kmeans.fit(df)
labels = kmeans.predict(df)

#calculates the centers of the clusters
centers = kmeans.cluster_centers_

# sets graph's x and y axis limits as well as labeling them
plt.xlim([3,6])
plt.ylim([0,5])
plt.xlabel('V1')
plt.ylabel('V2')
plt.title('V1 vs. V2')

# These display the colors of the clusters
color = 10 * ["black","blue","green", "purple", "orange"]
for i in range(len(df)):
    plt.scatter(df["V1"][i], df["V2"][i], color = color[labels[i]])

#These display the centers in the form of big red '+'
plt.scatter(centers[:, 1], centers[:, 2], color = "red", marker = '+', s = 150, linewidths = 5);

## displays the graph
plt.show()
