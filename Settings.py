import sys
from pathlib import Path
import os
import numpy as np
import pandas as pd

mature = True
insults = []
player = None
armory = None

def on_start(is_mature, current_player, current_armory):
    global mature
    global insults
    global player
    global armory
    mature = is_mature
    player = current_player
    armory = current_armory
    
    if mature:
        insults = pd.read_csv(get_root() + '/SortedInsults.csv')['Insults'].tolist()
    else:
        insults = pd.read_csv(get_root() + '/SortedClean.csv')['Insults'].tolist()
    

def quit():
    sys.exit()
    
def get_root():
    return str(Path(__file__).resolve().parent)

def wait():
    input()
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_insult():
    global insults
    return np.random.choice(insults)

def get_mature():
    global mature
    return mature

def get_player():
    global player
    return player

def get_armory():
    global armory
    return armory