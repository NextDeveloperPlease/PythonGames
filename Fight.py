import numpy as np
import pandas as pd
import Settings as st
from pathlib import Path

root_dir = str(Path(__file__).resolve().parent)
def fight(player):
    dogs = pd.read_csv(root_dir + '/Dogs.csv')
    dogs = dogs.columns
    num_dogs = 6
    
    selected_dogs = []
    for i in np.arange(num_dogs):
        selected_dogs.append(np.random.choice(dogs))
        
    winner = np.random.choice(selected_dogs)
    
    print(f"1. {selected_dogs[0]}  2. {selected_dogs[1]}")
    print(f"3. {selected_dogs[2]}  4. {selected_dogs[3]}")
    print(f"5. {selected_dogs[4]}  6. {selected_dogs[5]}")
    
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
        
    #print(winner)
    user_input = input("Choose one of the dogs: ").lower()
    
    if user_input == 'exit':
        return False
    elif user_input == 'quit':
        st.quit()
    if user_input == winner.lower():
        print("Congratulations!")
        player.add(bet * 4)
        print(player.get_wallet())
    else:
        print("Better luck next time.")
        player.spend(bet)
        print(player.get_wallet())
    return True
