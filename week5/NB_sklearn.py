from __future__ import division, print_function, unicode_literals
from sklearn.naive_bayes import MultinomialNB 
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.metrics import accuracy_score
import random

stopwords = ['', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

def read_library():
	infile = open('G:\\Github\\project2\\week5\\prepare_data\\library.txt', "r")
	split_string = infile.read().split()
	data = dict()
	for i in range(len(split_string)):
		data[split_string[i]] = i

	return data

def read_label(label_fn):
    with open(label_fn) as f:
        label = f.read().split()
    
    return np.array(label)
    

def count_word(stopwords, file, library):
    url = 'G:\\Github\\project2\\week5\\raw_data\\' + str(file) + '.txt'
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
train_data = []
k = 1
while (k != 41):
	print("file: ", k)
	d = count_word(stopwords, k, library)
	train_data.append(d)
	k = k + 1

train_data = np.array(train_data)
train_label = read_label('G:\\Github\\project2\\week5\\prepare_data\\label-training.txt')

clf = MultinomialNB()
clf.fit(train_data, train_label)

print('read history')
infile = open('G:\\Github\\project2\\week5\\prepare_data\\most-recently-read.txt', "r")
history = infile.read().split()
infile.close()
title_list = []

for i in range(len(history)):
	url = 'G:\\Github\\project2\\week5\\raw_data\\'+ history[i] + '.txt'
	infile = open(url, "r")
	title = infile.readline()
	infile.close()
	title = title.strip('n')
	title = title.strip('\\')
	title = title.strip()
	title_list.append(title)

group_list = []
for i in range(len(history)):
    test_data = []
    d = count_word(stopwords, history[i], library)
    test_data.append(d)
    test_data = np.array(test_data)
    if(str(clf.predict(test_data)[0]) == '0'):
        group_list.append('Science')
    else:
        group_list.append('Government,  Politics and Society')


print('\nYour newspaper reading history:\n')
for i in range(len(history)):
	print(title_list[i] + ' ---> ' + group_list[i])

n = len(history) - 1
print('\nThe article that was most recently read is :')
print(title_list[n] + ' ---> ' + group_list[n])

recomment = []
if(group_list[n] == 'Science'):
	while (len(recomment) != 3):
		random1 = random.randint(1, 20)
		if (str(random1) not in history) and (random1 not in recomment):
			recomment.append(random1)
else:
	while (len(recomment) != 3):
		random1 = random.randint(21, 40)
		if (str(random1) not in history) and (random1 not in recomment):
			recomment.append(random1)



print('\nYou may be interested:\n')
for i in range(len(recomment)):
    url = 'G:\\Github\\project2\\week5\\raw_data\\'+ str(recomment[i]) + '.txt'
    infile = open(url, "r")
    title = infile.readline()
    infile.close()
    title = title.strip('n')
    title = title.strip('\\')
    title = title.strip()
    print(title)


