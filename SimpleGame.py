from Race import *
from Fight import *
from Player import Player
from RussianRoulette import *
from Work import *
import Settings as st

running = True
mature = True

'''Six Options
    Gamble
    Work
    Pay Debt
    Get Loan
    Rob
    Check User's Stuff (Can be called in all the other locations as well)''' #Add a bar. What's the point of having money if you can't use it.
    
def gamble():
    if player.alive:
        user_input = input("1. Dog Race\t2. Dog Fight\n3. Roulette\t4. Russian Roulette\nType 'exit' to leave the casino. What would you like to do?\n")
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
    
def working():
    return work(player)

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

st.mature = input("Would you like mature settings?\nYes or no: ").lower() == 'yes'

city = ''
vice = ''
negative_outcome = ''
hangover = ''
if st.mature:
    city = 'Sin City'
    vice = "vice's"
    negative_outcome = 'die in a heap in an alley'
    hangover = ' and have a wicked hangover'
else:
    city = 'Heaven City'
    vice = "passion's"
    negative_outcome = 'wind up poor and in the dog house'

print(f"Welcome to {city}!\nPick your poison and let all your {vice} live wild!")
print(f"You must make the right choices and end up rich or {negative_outcome}.\nYour choices are free.")
print(f"You start out $10,000 in debt{hangover}.")
player = Player()
while running and player.alive:
    user_input = input("1. Gamble\t\t2. Work\n3. Pay your debt\t4. Get a loan\n5. Rob someone?\t\t6. Menu\n")
    match(user_input.lower()):
        case 'gamble':
            st.clear_screen()
            while gamble():''
        case 'work':
            st.clear_screen()
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