import random


class player:

    def __init__(self, playerid, location, name, balance):
        self.playerid = playerid
        self.location = location
        self.name = name
        self.balance = balance

    def play(self):
        method = input('which method you chooese? 1.card 2.dice')
        if method == 1:
            pass
        elif method == 2:
            moveSteps = random.randint(1, 6)
            self.location = self.location + moveSteps

    def playerLocation(self):
        return self.location
