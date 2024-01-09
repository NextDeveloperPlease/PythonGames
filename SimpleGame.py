import numpy as np
from Race import *
from Fight import *
from Player import Player
from RussianRoulette import *
from Work import *

running = True

'''Six Options
    Gamble
    Work
    Pay Debt
    Get Loan
    Rob
    Check User's Stuff (Can be called in all the other locations as well)''' #Add a bar. What's the point of having money if you can't use it.
    
def gamble():
    if player.alive:
        user_input = input("\n1. Dog Race\t2. Dog Fight\n3. Roulette\t4. Russian Roulette\nType 'exit' to leave the casino. What would you like to do?\n")
        match(user_input.lower()):
            case 'race': # This allows you to pick a dog for a race.
                race(player)
            case 'fight': # Pick a dog for a dog fight.
                fight(player)
            case 'roulette': # Pick red or black for roulette
                ""
            case 'russian': # Spin, aim at self, aim at wall
                russian(player)
            case 'exit':
                return False
            case 'quit':
                st.quit()
        return True

#def work():
    '''Work can escalate with your skill.'''
    '''Start as a horse manure worker.'''
    '''Get a position as horse hoover.'''
    '''Option to buy a horse (most of your money). If you gamble, it is worth it. Only way to progress'''
    '''Race your horse.'''
    '''Buy more horses and rig races'''
    
    #user_input = input("\n1. Work\t2. Request promotion\n3. Get paycheck\nWhat would you like to do?\n")
    #match(user_input.lower):
    #    case 'work': # Increments the clock by a fixed amount, adds funds to paycheck, increases boss's happiness (If done too many times, it will kill you.)
    #        ""
    #    case 'promotion': # Promotion if high enough happiness, otherwise boss's happiness decreases
    #        ""
    #    case 'paycheck': # If day matches payday, add money from paycheck to wallet (taxes aren't payed by the employee)
    #        ""
    #    case 'exit':
    #        return False
    #    case 'quit':
    #        player.quit()
    #return True
    
def working():
    return work(player)

def pay_debt():
    '''Here you pay your debt (starts at $1,000,000)'''
    user_input = input("How much would you like to pay? Enter amount here: ")
    if user_input == 'exit':
        return False
    elif user_input == 'quit':
        st.quit()
    try: # Checks if the user input is an integer, if so, add it to the user's bank account. 
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
    
def rob():
    '''Pick a location'''
    '''Parent's House: Easy'''
    '''Neighbor's House: Medium'''
    '''Rich Neighbor Down the Street: Hard'''
    
    user_input = input("\n1. Work\t2. Request promotion\n3. Get paycheck\nWhat would you like to do?\n")
    match(user_input.lower):
        case 'parents': # Tries to rob their parents. 60% chance vs 90% chance
            ""
        case 'neighbors': # Tries to rob their neighbor. 40% chance vs 75% chance
            ""
        case 'rich': # Tries to rob their rich neighbor. 10% chance vs 60% chance
            ""
        case 'exit':
            return False
        case 'quit':
            st.quit()
    return True

def menu(): # allows the user to check their money and items.
    ''

print("Welcome to Sin City!\nPick your poison and let all your vice's live wild!")
print("You must make the right choices and end up rich or die in a heap in an alley.\nYour choices are free.")
print("You start out $10,000 in debt and have a wicked hangover")
player = Player()
while running and player.alive:
    user_input = input("1. Gamble\t\t2. Work\n3. Pay your debt\t4. Get a loan\n5. Rob someone?\t\t6. Menu\n")
    match(user_input.lower()):
        case 'gamble':
            while gamble():''
        case 'work':
            while working(): ''
        case 'pay':
            pay_debt()
        case 'loan':
            get_loan()
        case 'rob':
            rob()
        case 'menu':
            menu()
        case 'quit':
            st.quit()
        case _:
            print("Sorry, I don't think I caught that")