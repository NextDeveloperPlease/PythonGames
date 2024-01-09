import sys
from pathlib import Path
import os
    
def quit():
    sys.exit()
    
def get_root():
    return str(Path(__file__).resolve().parent)

def wait():
    input()
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')