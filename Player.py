import sys
class Player:
    def __init__(self):
        self.wallet = 1000
        self.og_wallet = 1000
        self.alive = True
    
    def get_wallet(self):
        return self.wallet
    
    def spend(self, amount):
        self.wallet -= amount
        
    def add(self, amount):
        self.wallet += amount