from Gun import Gun
class Armory:
    def __init__(self):
        self.guns = [Gun(5, 'shotgun'), Gun(6, 'revolver'), Gun(8, '1911')]
    
    def add_gun(self, gun_type, capacity):
        self.guns.append(Gun(capacity, gun_type))
    
    def remove_gun(self, gun):
        self.guns.remove(gun)
        
    def get_gun(self): # Need to figure out a way to get the gun and return it to the player in russian roulette"
        print("Welcome to the armory. Which gun would you like?\n")
        for gun in self.guns:
            print("(" + (gun.get_gun_type() + ', ' + str(gun.get_capacity())) + ")") # Figure out a way to remove the final comma (makes it look nicer without it)
        
        
        user_input = input("\nSelection (format: revolver): ")
        gun = self.find_gun(user_input)
        return gun
        
    def find_gun (self, gun_type):
        for gun in self.guns:
            if gun_type == gun.get_gun_type():
                return gun
        return None
        
#a = Armory()
#current_gun = a.get_gun()
#print(current_gun)