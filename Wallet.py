class Wallet:
    def __init__(self, og_wallet_amount) -> None:
        self.og_wallet = og_wallet_amount
        self.wallet = og_wallet_amount
        
    def add(self, amount):
        self.wallet += amount
    
    def remove(self, amount):
        self.wallet -= amount
    
    def get_wallet(self):
        return self.wallet