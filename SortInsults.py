import csv
import os
import pandas as pd
import Settings as st

root_dir = st.get_root()

noun_file_path = root_dir + '/Nouns.csv'
adjective_file_path = root_dir + '/Adjectives.csv'
file_exists = os.path.isfile(noun_file_path)
file_exists = os.path.isfile(adjective_file_path)
count = 0
nouns = []
adjectives = []
with open(noun_file_path, 'r', newline='') as noun:
    reader = csv.reader(noun)
    nouns = [row[0] for row in reader]
with open(adjective_file_path, 'r', newline='') as adj:
    reader = csv.reader(adj)
    adjs = [row[0] for row in reader]
with open(root_dir + '/UnsortedInsults.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for adjective in adjs:
            for noun in nouns:
                writer.writerow([adjective + " " + noun])

unsorted_csv = root_dir + "/UnsortedInsults.csv"
   
df = pd.read_csv(unsorted_csv)
df.columns = ['Insults']
sorted_df = df.sort_values('Insults')
sorted_df.to_csv(root_dir + '/SortedInsults.csv', index=False)