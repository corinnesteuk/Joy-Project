
import pandas as pd
import json

'''Code to Combine Year JSON files'''        
file_a = [] #these should be the path to the file
file_b = []
file_combined  = []
with open(file_a, 'r') as f: #change this to file_b when done with file_a
    a = f.read() #reads it in as a text file
    f.flush()
with open(file_combined, 'a') as f:
    f.write(a)
    f.flush()
    

df = pd.read_json(file_combined)
df.tail()