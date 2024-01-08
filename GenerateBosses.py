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
        for i in np.arange(1000):
            writer.writerow([f'{np.random.choice(names)} {np.random.choice(names)}',np.random.randint(50,2000)])