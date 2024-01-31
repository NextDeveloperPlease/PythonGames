import numpy as np
import Settings as st
def betting(player):
    betting = True
    while betting: # I have written this four times. Add this to Settings so I can call it instead of retyping it.
        try:
            bet = int(input("Enter your bet: "))
        except:
            print(f'"Is mayonaise an instrument" looking {st.get_insult}')
        if bet > player.get_player_info('wallet') or bet < 0:
            print("You crook!")
            amount_lost = np.random.randint(1, 20)
            print(f"You lose: {amount_lost}")
            player.spend(amount_lost)
            print(player.get_player_info('wallet'))
        else:
            betting = False
    return bet