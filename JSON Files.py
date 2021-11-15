import pandas as pd
import json


j = pd.read_json('tweets-2019-09-02.json', lines = True)
j = j.drop(columns = ['_type', 'url', 'cashtags'])
#j = j.set_index(['id'])
print(j)

f2data = "" 

with open('tweets-2019-09-01.json') as f2: 
    f2data = '\n' + f2.read()
    
with open('tweets-2019-09-02.json','a+') as f1:
    f1.write(f2data)
    j2 = pd.read_json('tweets-2019-09-02.json', lines = True)
print(j2)