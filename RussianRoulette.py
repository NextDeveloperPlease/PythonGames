import numpy as np
import pandas as pd
import Settings as st
import CommonFunctions as cm
from Gun import Gun
from Armory import Armory

nsfw = "The explosion rings out before everyone\nnotices you slumped over in your chair.\nA pool starts forming on the table.\nYou Died"
sfw = "The bullet misses you by inches.\nYou realize life isn't worth this risk and leave.\nNo one knows where you went.\nGame Over"

def russian(player):
    user_input = input("Type exit to leave. Can't leave after this.\n")
    if user_input == 'exit':
        return False
    st.clear_screen()
    bet = cm.betting(player)
    
    gun = select_gun()
    
    multiplier = 1
    gun.load()
    while player.get_player_info('alive') and input("Do you pull the trigger? yes or no.\n") == 'yes': # Checks if the player pulls the trigger
        play(player, gun)
        pay_out(player, bet, multiplier)
        user_input = input('Do you want to reset the revolver? yes or no\n').lower() # Allows the player to reset the revolver
        if user_input == 'yes':
            gun.load()
            multiplier = 1
        else:
            multiplier = 4 * multiplier
        st.clear_screen()
     
'''This pulls the trigger on the gun and checks if it fires a blank or not. If it does, the player survives.
Otherwise, the player dies.'''
def play(player, gun):
    if gun.pull_trigger():
        print("Congratulations!")
        gun.check_ammo()
    else:
        player.alive = False
        print(nsfw if st.mature else sfw)
        st.quit()

def pay_out(player, bet, multiplier):
    player.add(bet * multiplier)
    print(player.get_player_info('wallet'))
    
'''Lists off the available guns to choose from and then lets the user pick their gun'''
def select_gun():
    armory = st.get_armory()
    gun = Gun(5)
    return gun