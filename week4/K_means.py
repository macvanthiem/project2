from __future__ import print_function
import numpy as np
from sklearn.cluster import KMeans


def read_library():
    infile = open('E:\\Github\\project2\\week4\\prepare_data\\library.txt', "r")
    split_string = infile.read().split()
    infile.close()
    data = dict()
    for i in range(len(split_string)):
        data[split_string[i]] = i

    return data

library = read_library()
print("read data training")
data = []
k = 1
while (k != 801):
    print("file: ", k)
    infile = open('E:\\Github\\project2\\week4\\preprocessing_data\\' + str(k) + '.txt', "r")
    d = infile.read().split()
    infile.close()
    for i in range(len(d)):
        d[i] = int(d[i])
    
    data.append(d)
    k = k + 1

data = np.array(data)

kmeans = KMeans(n_clusters = 2, random_state = 0).fit(data)
print('Centers found by scikit-learn:')
print(kmeans.cluster_centers_)
print('Solution')
print(kmeans.predict(data))
