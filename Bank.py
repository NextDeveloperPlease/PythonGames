import Settings as st
import pandas as pd

root_dir = st.get_root()
insults = ''
if st.mature:
    insults = pd.read_csv(root_dir + '/SortedInsults.csv')
else:
    insults = pd.read_csv(root_dir + '/SortedClean.csv')

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
            print(f"You don't have a loan you {insults}!")
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
        
        
        
    def pay_debt():
        '''Here you pay your debt (starts at $1,000,000)'''
        user_input = input("How much would you like to pay? Enter amount here: ")
        if user_input == 'exit':
            return False
        elif user_input == 'quit':
            st.quit()
        try: # Checks if the user input is an integer, if so, add it to the user's debt account. 
            user_input = int(user_input)
        except ValueError:
            print("Sorry, that wasn't an acceptable answer.")
        return True

    def get_loan():
        '''Get a loan with different rates'''
        '''Bank: 10% but you need high credit'''
        '''Loan Shark: 20% but it is the starting loan'''
        '''Large Loan Shark: 30% but can give the largest loan'''
        
        user_input = input("\n1. Request Bank loan(10%)\t2. Request loan shark loan(20%)\n3. Request large loan(30%)\nEach loan increments per move. What would you like to do?\n")
        match(user_input.lower):
            case 'bank': # Check if the user has a high enough credit, add money to their account and their debt count
                ""
            case 'shark': # Check if the user has another loan, add money to their account and their debt count
                ""
            case 'paycheck': # Check if the user has a high enough credit, add money to their account and their debt count
                ""
            case 'exit':
                return False
            case 'quit':
                st.quit()
        return True