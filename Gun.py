import numpy as np
import Settings as st

# Add an enum for the live and blank rounds. That way I only have to update one location to change stuff

class Gun:
    def __init__(self, gun_capacity, gun_type) -> None:
        self.gun_capacity = gun_capacity
        self.ammo_loaded = []
        self.gun_type = gun_type
    
    '''Takes a user input and fills the gun with that many live rounds. User input should be an integer.'''
    def load(self):
        self.ammo_loaded = []
        loaded = False
        while not loaded:
            live_ammo_count = input("Enter the number of live bullets: ")
            try:
                live_ammo_count = int(live_ammo_count)
            except:
                print("That isn't a number. Try again.")
                continue
            if live_ammo_count > self.gun_capacity:
                print(f"That amount is greater than your guns ammo capacity.\nYou chose {live_ammo_count} when your gun only holds {self.gun_capacity}.\nTry again.")
                continue
            if live_ammo_count == self.gun_capacity:
                suicide = input("You have loaded the gun with only live rounds.\nWould you like to contine? Yes or no\n").lower()
                if suicide == 'yes':
                    loaded = True
                continue
            loaded = True
        for i in np.arange(live_ammo_count):
            self.ammo_loaded.append('live')
        if self.gun_capacity - live_ammo_count > 0:
            for i in np.arange(self.gun_capacity - live_ammo_count):
                self.ammo_loaded.append('blank')
    
    '''Randomly chooses a value from "ammo_loaded". Returns whether it was blank or not'''
    def pull_trigger(self):
        '''Chooses a random choice from the gun's ammo. If live, you die.'''
        print('You pull the trigger...')
        st.wait()
        return_value = True
        removal = ''
        if np.random.choice(self.ammo_loaded) == 'live':
            removal = 'live'
            print('BANG!!!')
            return_value = False
        else:
            removal = 'blank'
            print('click!!!')
            return_value = True
        st.wait()
        self.ammo_loaded.remove(removal)
        return return_value
    
    '''Prints out what is loaded in the gun (not necessarily the order it will be chosen)'''
    def check_ammo(self):
        print(self.ammo_loaded)
        
    def get_gun_type(self):
        return self.gun_type
    
    def get_capacity(self):
        return self.gun_capacity