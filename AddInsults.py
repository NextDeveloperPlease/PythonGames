import csv
import pandas as pd
import os
import Settings as st

root_dir = st.get_root()
insults_file = root_dir + '/Insults.csv'
file_exists = os.path.isfile(insults_file)
with open(insults_file, 'a', newline='\n') as file:
    writer = csv.writer(file)

    # Input insults and write them to the file
    insult = ''
    while insult.lower() != 'quit':  # Use lower() to handle 'Quit' or 'QUIT' as well
        insult = input("Enter insult here (or 'quit' to stop): ")
        if insult.lower() != 'quit':
            writer.writerow([insult])  # Write the insult as a single-element list
print("Insults have been added to the file.")

'''
import csv
import os
import numpy as np

csv_file_path = 'Bosses1.csv'
file_exists = os.path.isfile(csv_file_path)
count = 0
names = []
with open('Names.csv', 'r', newline='') as name:
    reader = csv.reader(name)
    names = [row[0] for row in reader]
with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for i in np.arange(100):
            writer.writerow([f'{np.random.choice(names)} {np.random.choice(names)}',np.random.randint(50,2000)])'''