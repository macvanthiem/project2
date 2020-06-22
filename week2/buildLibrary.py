results = []
stopwords = ['','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

def count_word(mylist, file):
    infile = open(file, encoding="utf8")
    split_string = list(set(infile.read().split()))
    for i in range(len(split_string)):
        split_string[i] = split_string[i].lower()
        split_string[i] = split_string[i].strip('.')
        split_string[i] = split_string[i].strip(',')
        split_string[i] = split_string[i].strip(';')
        split_string[i] = split_string[i].strip(':')
        split_string[i] = split_string[i].strip('(')
        split_string[i] = split_string[i].strip(')')
        split_string[i] = split_string[i].strip('-')
        split_string[i] = split_string[i].strip('!')
        split_string[i] = split_string[i].strip('?')
        split_string[i] = split_string[i].strip('\'')
        split_string[i] = split_string[i].strip('"')


    mylist.extend(split_string)
    infile.close()

def removeStopWord(results, stopwords):
    content = []
    for i in results:
        if i not in stopwords:
            content.append(i)

    return content

def makeUrl(filename):
    url = 'E:\\Github\\project2\\week2\\dataset\\' + str(filename) + '.txt'
    return url

k = 1
while (k != 849):
    print("file: " + str(k))
    filename = makeUrl(k)
    count_word(results, filename)
    k = k + 1

results = list(set(results))
results = removeStopWord(results, stopwords)

with open('E:\\Github\\project2\\week2\\prepare_data\\library.txt', "w") as outfile:
    for result in results:
        outfile.write(result + ' ')

