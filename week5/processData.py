stopwords = ['', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

def read_library():
	infile = open('G:\\Github\\project2\\week5\\prepare_data\\library.txt', "r")
	split_string = infile.read().split()
	data = dict()
	for i in range(len(split_string)):
		data[split_string[i]] = i

	return data

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

    #write file
    outfile = open('G:\\Github\\project2\\week5\\prepare_data\\data-training.txt', 'a')
    for i in data:
    	outfile.write(str(file))
    	outfile.write(' ')
    	outfile.write(str(library[i]))
    	outfile.write(' ')
    	outfile.write(str(data[i]))
    	outfile.write('\n')

    outfile.close()




library = read_library()
# count_word(stopwords, 11, library)

k = 40
while (k != 0):
    print(k)
    count_word(stopwords, k, library)
    k = k - 1

