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
    
    def spend(self, amount):
        self.wallet -= amount
        
    def add(self, amount):
        self.wallet += amount
    
    def set_job(self, job): #name,rapport_required,job,duration,pay,rapport,skill_increased,skill_required
        job_values = job.values.tolist()[0]
        print(f"You work at ")
        print(job_values) # Change this to look good!!!
        self.job = job
        self.boss_name = job_values[0]
        self.job_name = job_values[2]
        self.duration = job_values[3]
        self.pay = job_values[4]
        self.rapport_increased = job_values[5]
        self.skill_increased = job_values[6]
        converted = time.convert(self.duration)
        print(f"You work for {self.boss_name} as a {self.job_name}.\nYou work {converted[0]} hours and {converted[1]} minutes a day at ${self.pay} an hour.")
    
    def quit_job(self):
        self.job = None
        self.boss_name = None
        self.job_name = None
        self.duration = None
        self.pay = None
        self.rapport_increased = None
        self.skill_increased = None
        
    def increase_skill(self, skill):
        self.skill += skill

    def get_player_info(self, info):
        match(info):
            case 'job': return self.job
            case 'wallet': return self.wallet
            case 'og_wallet': return self.og_wallet
            case 'alive': return self.alive
            case 'clock': return self.clock
            case 'skill': return self.skill
            case 'boss_name': return self.boss_name
            case 'job_name': return self.job_name
            case 'duration': return self.duration
            case 'pay': return self.pay
            case 'rapport_increased': return self.rapport_increased
            case 'skill_increased': return self.skill_increased
            case 'skill': return self.skill