import numpy as np
import pandas as pd
import Settings as st

root_dir = st.get_root()
mature = st.mature

def race(player):
    st.clear_screen()
    dogs = pd.read_csv(root_dir + '/Dogs.csv')
    dogs = dogs.columns
    num_dogs = 4
    
    
    selected_dogs = []
    for i in np.arange(num_dogs):
        selected_dogs.append(np.random.choice(dogs))
    winner = np.random.choice(selected_dogs)
    
    print(f"1. {selected_dogs[0]}  2. {selected_dogs[1]}")
    print(f"3. {selected_dogs[2]}  4. {selected_dogs[3]}")
    
    betting = True
    bet = 0
    while betting:
        bet = (input("Enter your bet: "))
        try:
            bet = int(bet)
            if bet > player.get_player_info('wallet'):
                print("You crook!")
                amount_lost = np.random.randint(1, 20)
                print(f"You lose: {amount_lost}")
                player.spend(amount_lost)
                print(player.get_player_info('wallet'))
            else:
                betting = False
        except:
            print("That isn't a bet. Try again")
        
    #print(winner)
    user_input = input("Choose one of the dogs: ").lower()
    if user_input == 'exit':
        return False
    elif user_input == 'quit':
        st.quit()
    if user_input == winner.lower():
        print("Congratulations!")
        player.add(bet)
        print(player.get_player_info('wallet'))
    else:
        print("Better luck next time.")
        player.spend(bet)
        print(player.get_player_info('wallet'))
    st.wait()
    return True
