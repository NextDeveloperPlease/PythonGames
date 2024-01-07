import numpy as np
import pandas as pd
import Settings as st
def russian(player):
    reset_revolver=['safe', 'safe', 'safe', 'safe', 'safe', 'death']
    revolver = reset_revolver
    user_input = input("Type exit to leave. Can't leave after this.\n")
    if user_input == 'exit':
        return False
    elif user_input == 'quit':
        st.quit()
    betting = True
    bet = 0
    while betting:
        bet = int(input("Enter your bet: "))
        if bet > player.get_wallet():
            print("You crook!")
            amount_lost = np.random.randint(1, 20)
            print(f"You lose: {amount_lost}")
            player.spend(amount_lost)
            print(player.get_wallet())
        else:
            betting = False
    
    running = True   
    while running and input("Do you pull the trigger? yes or no.\n") == 'yes':
        running = play(player, revolver, bet)
        if running:
            user_input = input('Do you want to reset the revolver? yes or no\n').lower()
            if user_input == 'yes':
                revolver = reset_revolver
    

def play(player, revolver, bet):
    if np.random.choice(revolver) == 'death':
        player.alive = False
        return False
    else:
        print("Congratulations!")
        player.add(bet)
        print(player.get_wallet())
        revolver.remove('safe')
        print(revolver)
        return True