import random
from dice import dice


class player:

    def __init__(self, playerid, location, name, balance, direction):
        self.playerid = playerid
        self.location = location
        self.name = name
        self.balance = balance
        self.direction=direction

    def play(self):
        method = input('which method you chooese? 1.card 2.dice')
        if method == 1:
            pass

        elif method == 2:    
            shakeDice = dice()
            moveSteps = shakeDice.roll(1)
            return self.direction*moveSteps

    def set_location(self, location):
    	self.location = location

    def playerLocation(self):
        return self.location
