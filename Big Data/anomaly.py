import numpy as np
import statistics

#this function returns the ith column in a 2D list A
def get_col(A, i):
    return [float(row[i]) for row in A]

#==============================================================

#open the file
file = open("mammal_sleep_1.txt")

#read the file into a matrix
attributes = [line.rstrip().split("\t") for line in file]

#create an array to hold the mean of each attribute
attribute_mean = []
attribute_standard_deviation = []
count = 1

#get each column (attribute) in the matrix
for i in range ( 1, len(attributes[0])):

    #extract all the attribute values into an array attribute_array
    attribute_array = get_col(attributes, i)
    if count == 1:
        attribute1 = attribute_array
    elif count == 2:
        attribute2 = attribute_array
    elif count == 3:
        attribute3 = attribute_array
    elif count == 4:
        attribute4 = attribute_array
    elif count == 5:
        attribute5 = attribute_array
    elif count == 6:
        attribute6 = attribute_array
    elif count == 7:
        attribute7 = attribute_array
    elif count == 8:
        attribute8 = attribute_array
    elif count == 9:
        attribute9 = attribute_array
    elif count == 10:
        attribute10 = attribute_array
        
    
    #compute mean
    attribute_mean.append(np.mean(attribute_array))
    print(attribute_array)
    
    
    #compute stdev
    attribute_standard_deviation.append(statistics.stdev(attribute_array))
    
    
    #for each entry in attribute_mean, check whether it is an anomaly, print anomalous values.
    for v in range(1, 10):
        m = np.mean(attribute_array)
        s = statistics.stdev(attribute_array)
        if (v > m + (2 * s)):
            print("This attribute has an an anomalous value of {}".format(v))
        elif (v < m - (2 * s)):
            print("This attribute has an an anomalous value of {}".format(v))

    print("Attribute mean =  ", np.mean(attribute_array))
    print("Attribute standard deviation = ", statistics.stdev(attribute_array))
    
    count += 1

count = count - 1
print(attribute1)
print(attribute2)
print(attribute3)
print(attribute4)
print(attribute5)
print(attribute6)
print(attribute7)
print(attribute8)
print(attribute9)
print(attribute10)
print("There are {} attributes.".format(count))
print("The attribute means are: ", attribute_mean)
print("The standard deviations are: ", attribute_standard_deviation)