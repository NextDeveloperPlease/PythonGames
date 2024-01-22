import numpy as np
import pandas as pd
import Settings as st

nsfw = "The explosion rings out before everyone\nnotices you slumped over in your chair.\nA pool starts forming on the table.\nYou Died"
sfw = "The bullet misses you by inches.\nYou realize life isn't worth this risk and leave.\nNo one knows where you went.\nGame Over"

def russian(player): ############ Add create_gun() to this.
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
    
def create_gun():
    gun = []
    chosen = False
    filled = False
    guns = {
        'revolver': 6,
        'shotgun': 5,
        '1911': 7,
    }
    gun_capacity = 0
    while not chosen:
        gun_choice = input("Which gun would you like to use? (Revolver, Shotgun, 1911)\n").lower()
        try:
            gun_capacity = guns[gun_choice]
            chosen = True
        except:
            print("Sorry, that wasn't an allowed choice")
    
    while not filled:
        live_ammo_count = input("Enter the number of live bullets: ")
        try:
            live_ammo_count = int(live_ammo_count)
        except:
            print("That isn't a number. Try again.")
            continue
        if live_ammo_count > gun_capacity:
            print(f"That amount is greater than your guns ammo capacity.\nYou chose {live_ammo_count} when your gun only holds {gun_capacity}.\nTry again.")
            continue
        if live_ammo_count == gun_capacity:
            suicide = input("You have loaded the gun with only live rounds.\nWould you like to contine? Yes or no\n").lower()
            if suicide == 'yes':
                filled = True
            continue
        filled = True
        
    for _ in np.arange(live_ammo_count):
        gun.append('live')
    for _ in np.arange(gun_capacity - live_ammo_count):
        gun.append('blank')
    return gun

def calculate_multiplier(): # Finish this
    ''
    
print(create_gun())