"""
Author: Tousif Chowdhury
Description: A simple class to store the cluster information.
"""

class Node:

    """
    Take in a list of recordIds and attributes.
    Has properties:
    recordId: List of recordIds in the cluster
    records: List of attributes for the record
    realId: The smallest recordId to classify the merged clusters
    centerOfMass: Array of points that represent the center
    size: The number of records in the cluster
    """
    def __init__(self, recordId, attributes):
        recordIds = []
        for item in recordId:
            recordIds.append(item)

        self.recordIds = recordIds

        records = []
        for item in attributes:
            records.append(item)

        self.records = records
        self.realId = min(self.recordIds)
        self.centerOfMass = self.calculateCenterofMass()
        self.size = len(self.records)

    """
    Function to combine one cluster into this cluster.
    Append the ids and the attributes.
    """
    def combine(self,listOfIds,listofAttributes):
        for item in listofAttributes:

            self.records.append(item)

        for item in listOfIds:
            self.recordIds.append(item)


    """
    Function to calculate the center of mass.
    """
    def calculateCenterofMass(self):
        sums = [0,0,0,0,0,0,0,0,0,0,0,0]
        for record in self.records:
            for i in range(0,12):
                sums[i] += record[i]

        for item in sums:
            item /= len(self.records)
        self.centerOfMass = sums





