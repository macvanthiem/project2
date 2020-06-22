from __future__ import division, print_function, unicode_literals
from sklearn.naive_bayes import MultinomialNB 
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.metrics import accuracy_score
import random

def read_label(label_fn):
    with open(label_fn) as f:
        label = f.read().split()
    
    return np.array(label)  

print("read data training")
train_data = []
k = 1
while (k != 801):
    print("file: ", k)
    infile = open('E:\\Github\\project2\\week2\\preprocessing_data\\' + str(k) + '.txt', "r")
    d = infile.read().split()
    for i in range(len(d)):
        d[i] = int(d[i])
    
    infile.close()
    train_data.append(d)
    k = k + 1

train_data = np.array(train_data)
train_label = read_label('E:\\Github\\project2\\week2\\prepare_data\\label-training.txt')
clf = MultinomialNB()
clf.fit(train_data, train_label)

print('read history')
infile = open('E:\\Github\\project2\\week5\\prepare_data\\most-recently-read.txt', "r")
history = infile.read().split()
infile.close()
title_list = []

for i in range(len(history)):
	url = 'E:\\Github\\project2\\week2\\dataset\\' + history[i] + '.txt'
	infile = open(url, "r")
	title = infile.readline()
	infile.close()
	title = title.strip('n')
	title = title.strip('\\')
	title = title.strip()
	title_list.append(title)

group_list = []
for i in range(len(history)):
    infile = open('E:\\Github\\project2\\week2\\preprocessing_data\\' + history[i] + '.txt', "r")
    test_data = []
    d = infile.read().split()
    for i in range(len(d)):
        d[i] = int(d[i])

    infile.close()
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
		random1 = random.randint(401, 800)
		if (str(random1) not in history) and (random1 not in recomment):
			recomment.append(random1)
else:
	while (len(recomment) != 3):
		random1 = random.randint(1, 400)
		if (str(random1) not in history) and (random1 not in recomment):
			recomment.append(random1)



print('\nYou may be interested:\n')
for i in range(len(recomment)):
    url = 'E:\\Github\\project2\\week2\\dataset\\'+ str(recomment[i]) + '.txt'
    infile = open(url, "r")
    title = infile.readline()
    infile.close()
    title = title.strip('n')
    title = title.strip('\\')
    title = title.strip()
    print(title)


