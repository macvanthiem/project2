import csv
import numpy as np
dataset = []
with open('E:\\Github\\project2\\week6\\datasets_264386_555058_groceries - groceries.csv','rt')as f:
    data = csv.reader(f)
    i = 0
    for row in data:
        x = []
        if (i != 0):
            for j in range(1,len(row)):
                if (row[j] != ''):
                    x.append(row[j])
            dataset.append(x)
        i += 1

dataset = np.array(dataset)

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.02, use_colnames=True)
# frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
# print(frequent_itemsets[ (frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.03) ])
from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
print(rules)
