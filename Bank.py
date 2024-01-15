import Settings as st

mature = st.mature

'''Maybe rewrite this'''

class Bank:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.principle = self.initial_principle = 0
        self.has_loan = False
        self.has_account = False
        
    def get_loan(self, principle):
        self.principle = principle
        print(f"You have a ${self.principle} loan with an interest rate of {self.rate}")
        
    def calculate_interest(principle, rate, time=(1/365), num_per_year=365):
        future_value = principle * (1 + rate/num_per_year) ** (time * num_per_year)
        return future_value
    
    def apply_interest(self):
        if self.principle == 0:
            print("You don't have a loan you dumbass!")
        else:  
            self.principle = self.calculate_interest(self.principle, self.rate)
    
    def pay_loan(self, amount):
        if not self.has_loan:
            return False
        self.principle -= amount
        
    def create_bank_account(self, initial_amount):
        if self.has_account:
            print("You already have an account.")
            return False
        self.principle = initial_amount