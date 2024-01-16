import numpy as np
import pandas as pd
import Settings as st

nsfw = "The explosion rings out before everyone\nnotices you slumped over in your chair.\nThe wall behind you is painted red.\nA pool starts forming on the table.\nYou Died"
sfw = "The bullet misses you by inches.\nYou realize life isn't worth this risk and leave.\nNo one knows where you went.\nGame Over"

def russian(player):
    reset_revolver=['safe', 'safe', 'safe', 'safe', 'safe', 'death'] # defines the revolver (future update: I might change this so it can be variable)
    revolver = reset_revolver.copy()
    user_input = input("Type exit to leave. Can't leave after this.\n")
    if user_input == 'exit':
        return False
    st.clear_screen()
    betting = True
    bet = 0
    while betting: # I have written this four times. Add this to Settings so I can call it instead of retyping it.
        bet = int(input("Enter your bet: "))
        if bet > player.get_player_info('wallet'):
            print("You crook!")
            amount_lost = np.random.randint(1, 20)
            print(f"You lose: {amount_lost}")
            player.spend(amount_lost)
            print(player.get_player_info('wallet'))
        else:
            betting = False
    
    multiplier = 1
    while player.get_player_info('alive') and input("Do you pull the trigger? yes or no.\n") == 'yes': # Checks if the player pulls the trigger
        play(player, revolver, bet, multiplier)
        user_input = input('Do you want to reset the revolver? yes or no\n').lower() # Allows the player to reset the revolver
        if user_input == 'yes':
            revolver = reset_revolver.copy()
            multiplier = 1
        else:
            multiplier = 4 * multiplier
        print(revolver)
        st.wait()
    

def play(player, revolver, bet, multiplier):
    '''Chooses a random choice from the revolver's ammo. If death, you die.'''
    print('You pull the trigger...')
    st.wait()
    if np.random.choice(revolver) == 'death':
        player.alive = False
        print(nsfw if st.mature else sfw)
        st.quit()
    else:
        print('click!!!')
        st.wait()
        print("Congratulations!")
        player.add(bet * multiplier)
        print(player.get_player_info('wallet'))
        revolver.remove('safe')
        print(revolver)
        return True