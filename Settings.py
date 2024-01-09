import sys
from pathlib import Path
    
def quit():
    sys.exit()
    
def get_root():
    return str(Path(__file__).resolve().parent)