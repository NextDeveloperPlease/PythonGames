from Clock import time
import Settings as st
from Wallet import Wallet

class Player:
    def __init__(self):
        self.wallet = Wallet(1000)
        self.alive = True
        self.clock = time()
        self.job = None
        self.skill = 0
        self.boss_name = None
        self.job_name = None
        self.duration = None
        self.pay = None
        self.rapport_required = None
        self.rapport_increased = None
        self.rapport = 0
        self.skill_required = None
        self.skill_increased = None
    
    def spend(self, amount):
        self.wallet.remove(amount)
        
    def add(self, amount):
        self.wallet.add(amount)
    
    def set_job(self, job): #name,rapport_required,job,duration,pay,rapport,skill_increased,skill_required
        job_values = job.values.tolist()[0]
        self.job = job
        self.boss_name = job_values[0]
        self.rapport_required = int(job_values[1])
        self.job_name = job_values[2]
        self.duration = int(job_values[3])
        self.pay = int(job_values[4])
        self.rapport_increased = int(job_values[5])
        self.skill_increased = int(job_values[6])
        self.skill_required = int(job_values[7])
        converted = time.convert(self.duration)
        print(f"You work for {self.boss_name} as a {self.job_name}.\nYou work {converted[0]} hours and {converted[1]} minutes a day at ${self.pay} an hour.")    
    
    def quit_job(self):
        self.job = None
        self.boss_name = None
        self.job_name = None
        self.duration = None
        self.pay = None
        self.rapport_required = None
        self.skill_required = None
        
    def increase_skill(self):
        self.skill += self.skill_increased

    def increase_rapport(self, rapport):
        self.rapport += rapport
        
    def increase_pay(self, amount):
        self.pay += amount
        self.job['pay'] = self.pay

    def get_player_info(self, info):
        match(info):
            case 'job': return self.job
            case 'wallet': return self.wallet.get_wallet()
            case 'og_wallet': return self.og_wallet
            case 'alive': return self.alive
            case 'clock': return self.clock
            case 'skill': return self.skill
            case 'boss_name': return self.boss_name
            case 'job_name': return self.job_name
            case 'duration': return self.duration
            case 'pay': return self.pay
            case 'rapport_required': return self.rapport_required
            case 'rapport_increased': return self.rapport_increased
            case 'rapport': return self.rapport
            case 'skill_required': return self.skill_required
            case 'skill_increased': return self.skill_increased
            case 'skill': return self.skill