from Clock import time
class Player:
    def __init__(self):
        self.wallet = 1000
        self.og_wallet = 1000
        self.alive = True
        self.clock = time()
        self.job = None
        self.skill = 2000
        self.boss_name = None
        self.job_name = None
        self.duration = None
        self.pay = None
        self.rapport_increased = None
        self.skill_increased = None
    
    def get_wallet(self):
        return self.wallet
    
    def spend(self, amount):
        self.wallet -= amount
        
    def add(self, amount):
        self.wallet += amount
    
    def get_job(self):
        return self.job
    
    def set_job(self, job): #name,rapport_required,job,duration,pay,rapport,skill_increased,skill_required
        self.job = job
        self.boss_name = job['name']
        self.job_name = job['job']
        self.duration = job['duration']
        self.pay = job['pay']
        self.rapport_increased = job['rapport']
        self.skill_increased = job['skill_increased']
        
    def increase_skill(self, skill):
        self.skill += skill
        
    def get_skill_level(self):
        return self.skill