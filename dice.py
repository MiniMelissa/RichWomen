import random
import os

class dice:
    seed = 0
    
    #############################################
    # Initialize                                #
    # seed:     set game random seed, optional  #
    #############################################

    def __init__(self, seed=-1):
        if seed != -1:
            self.seed = seed
        random.seed(self.seed)

    #################################################
    # Roll a dice                                   #
    # amount:   times of rolling dice               #
    # value:    roll out a defined value, optinal   #
    #################################################
    
    def roll(self, amount, value=-1):
        if value != -1:
            return value

        value = 0
        while True:
            if random.randint(1,10) % 2 == 0:
                value += random.SystemRandom().randint(1, 6)
            else:
                value += random.randint(1, 6)
            amount -= 1
            if amount == 0:
                break

        return value


if __name__ == "__main__":

    # randomness test
    d = dice()
    value = 0
    count = 100000 
    for i in range(0, count):
        value += d.roll(1)

    print float(value)/count
