from __future__ import division, print_function, unicode_literals
from sklearn.naive_bayes import MultinomialNB 
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.metrics import accuracy_score

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

print("read data test")
test_data = []
k = 801
while (k != 849):
    print("file: ", k)
    infile = open('E:\\Github\\project2\\week2\\preprocessing_data\\' + str(k) + '.txt', "r")
    d = infile.read().split()
    for i in range(len(d)):
        d[i] = int(d[i])
    
    infile.close()
    test_data.append(d)
    k = k + 1


test_data = np.array(test_data)
test_label = read_label('E:\\Github\\project2\\week2\\prepare_data\\label-test.txt')

clf = MultinomialNB()
clf.fit(train_data, train_label)

# if (str(clf.predict(test_data)[0]) == '1'):
# 	print("Science")
# else:
# 	print("Society")

y_pred = clf.predict(test_data)
print('Accuracy = %.2f%%' % (accuracy_score(test_label, y_pred)*100))
