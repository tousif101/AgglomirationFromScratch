"""
Author: Tousif Chowdhury

Description: Performs Agglomerative Clustering on datasets
"""
import pandas as pd
from clusterclass import Node
import math
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy
"""
Read in the CSV file into a list.
"""
df = pd.read_csv('shoppingdata.csv', delimiter=',')
listOfData = [list(x) for x in df.values]

"""
Function to calculate the euclidian distance between two points
"""
def calculateDistance(list1, list2):
    counter = 0
    for i in range(0,len(list1)):
        value = list1[i] - list2[i]
        valueSquare = math.pow(value,2)
        counter = counter + valueSquare

    euclid = math.sqrt(counter)

    return euclid

"""
Take the dataset and make Cluster classes out of them, orginally each cluster being each record.
Make a list of 100 clusters.
"""
listOfClusters= []
for i in range(0,len(listOfData)):
    cluster = Node([listOfData[i][0]],[listOfData[i][1:13]])
    listOfClusters.append(cluster)

"""
Quickly go through and set the center of mass for each cluster in the begining.
"""
for item in listOfClusters:
    item.calculateCenterofMass()

"""
Start the loop to begin the clustering process.
"""
while len(listOfClusters) > 3:

    smaller_cluster = 0
    larger_cluster = 0
    bestDistance = 1000000

    """
    Loop through both the clusters. Calculate the distance for every instance. At every instance though,
    Find the best distance. Simple if check. Figure out which one of the clusters is larger or smaller.
    """
    for clusterOne in listOfClusters:
        for clusterTwo in listOfClusters:
            if clusterOne != clusterTwo:
                dist = calculateDistance(clusterOne.centerOfMass,clusterTwo.centerOfMass)
                if dist < bestDistance:
                    bestDistance = dist
                    if clusterOne.size <= clusterTwo.size:
                        smaller_cluster = clusterOne
                        larger_cluster = clusterTwo
                    else:
                        smaller_cluster = clusterTwo
                        larger_cluster = clusterOne

    """
    Remove both the clusters from the list, combine the larger one into the smaller one,
    Add the merged one back into the list. Kepp going until 3 items left.
    """
    listOfClusters.remove(smaller_cluster)
    listOfClusters.remove(larger_cluster)
    smaller_cluster.combine(larger_cluster.recordIds,larger_cluster.records)
    listOfClusters.append(smaller_cluster)

"""
Quick print to see the results of the clustering
"""
print("Clusters Remaining are " + str(len(listOfClusters)))
for item in listOfClusters:
    print("------------------------------------")
    print("The Center of Mass is")
    print(item.centerOfMass)
    print("The shoppers in this cluster are")
    print(item.recordIds)

"""
Set up the scy py plot and linkages
"""
values = []
for item in listOfData:
    val = item[1:13]
    values.append(val)

arrayData = numpy.array(values)

Z = linkage(arrayData, 'median','euclidean')

plt.title('Aglomerative Clustering Dendorogram')
dendrogram(Z,truncate_mode='lastp',p=12,show_leaf_counts=False,show_contracted=True)
plt.xlabel("Record Number")
plt.ylabel("Attribute")
plt.show()


