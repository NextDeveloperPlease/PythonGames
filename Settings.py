import sys
from pathlib import Path
import os
import numpy as np
import pandas as pd

mature = True
insults = []

def quit():
    sys.exit()
    
def get_root():
    return str(Path(__file__).resolve().parent)

def wait():
    input()
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_mature(is_mature=True):
    global mature
    mature = is_mature
    
def set_insult():
    global insults
    if mature:
        insults = pd.read_csv(get_root() + '/SortedInsults.csv')['Insults'].tolist()
    else:
        insults = pd.read_csv(get_root() + '/SortedClean.csv')['Insults'].tolist()

def get_insult():
    global insults
    return np.random.choice(insults)