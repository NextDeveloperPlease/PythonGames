from Clock import time
class Player:
    def __init__(self):
        self.wallet = 1000
        self.og_wallet = 1000
        self.alive = True
        self.clock = time()
        self.job = None
        self.skill = -1
    
    def get_wallet(self):
        return self.wallet
    
    def spend(self, amount):
        self.wallet -= amount
        
    def add(self, amount):
        self.wallet += amount
    
    def get_job(self):
        return self.job
    
    def set_job(self, job):
        self.job = job
        
    def increase_skill(self, skill):
        self.skill += skill
        
    def get_skill_level(self):
        return self.skill