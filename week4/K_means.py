from __future__ import print_function
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

stopwords = ['', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

def read_library():
	infile = open('G:\\Github\\project2\\week4\\prepare_data\\library.txt', "r")
	split_string = infile.read().split()
	data = dict()
	for i in range(len(split_string)):
		data[split_string[i]] = i

	return data
    

def count_word(stopwords, file, library):
    url = 'G:\\Github\\project2\\week4\\raw_data\\' + str(file) + '.txt'
    infile = open(url, "r")
    split_string = infile.read().split()
    infile.close()


    #remove punctuation
    for i in range(len(split_string)):
        split_string[i] = split_string[i].lower()
        for i in range(len(split_string)):
            split_string[i] = split_string[i].lower()
            split_string[i] = split_string[i].strip('(')
            split_string[i] = split_string[i].strip(')')
            split_string[i] = split_string[i].strip('-')
            split_string[i] = split_string[i].strip('!')
            split_string[i] = split_string[i].strip(':')
            split_string[i] = split_string[i].strip('?')
            split_string[i] = split_string[i].strip('.')
            split_string[i] = split_string[i].strip(',')
            split_string[i] = split_string[i].strip(';')
            split_string[i] = split_string[i].strip('\'')
            split_string[i] = split_string[i].strip('"')

    #remove stopword
    content = []
    for i in split_string:
        if i not in stopwords:
            content.append(i)
    
    
    #count word
    data = dict()
    for i in range(len(content)):
    	data[content[i]] = 0

    for i in content:
        if i in data:
            data[i]+=1

    result = []
    for key in library:
    	if key in data:
    		result.append(data[key])
    	else:
    		result.append(0)

    return result


library = read_library();
print("read data training")
data = []
k = 1
while (k != 41):
	print("file: ", k)
	d = count_word(stopwords, k, library)
	data.append(d)
	k = k + 1

data = np.array(data)
# print("read data test: ")
# test = []
# d = count_word(stopwords, 48, library)
# test.append(d)
# test = np.array(test)

kmeans = KMeans(n_clusters = 2, random_state = 0).fit(data)
print('Solution')
print(kmeans.predict(data))
