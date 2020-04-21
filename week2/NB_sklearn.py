from __future__ import division, print_function, unicode_literals
from sklearn.naive_bayes import MultinomialNB 
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.metrics import accuracy_score

stopwords = ['', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

def read_library():
	infile = open('G:\\Python\\ML\\NB\\prepare_data\\library.txt', "r")
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
    url = 'G:\\Python\\ML\\NB\\raw_data\\' + str(file) + '.txt'
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

train_data = []
k = 1
while (k != 41):
	print("read data: ", k)
	d = count_word(stopwords, k, library)
	train_data.append(d)
	k = k + 1

train_data = np.array(train_data)
train_label = read_label('G:\\Python\\ML\\NB\\prepare_data\\label-training.txt')

test_data = []
d = count_word(stopwords, 48, library)
test_data.append(d)
test_data = np.array(test_data)

clf = MultinomialNB()
clf.fit(train_data, train_label)

if (str(clf.predict(test_data)[0]) == '1'):
	print("Science")
else:
	print("Society")

# y_pred = clf.predict(test_data)
# print('Accuracy = %.2f%%' % (accuracy_score(test_label, y_pred)*100))
