from Gun import Guns as g
import numpy as np

class GunStore:
    def __init__(self):
        self.possible_guns = g

    def randomizer(self):
        np.random.randint(5, 30)
        return 