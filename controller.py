from map import district
from player import player
import random

class controller:

    def __init__(self, mapsize, playersize, wintype, gameround):
        self.psize = playersize
        self.wtype = wintype
        self.round = gameround

        # TODO: Initial players and map
        self.players = []
        self.map = district(mapsize)
        self.msize = self.map.msize

        for i in range(0, self.psize):
            tmpPlayer = player(i, random.randint(0, self.msize), None, 0)
            self.players.append(tmpPlayer)

    def gamebegin(self):
        if self.wtype == 'dead':
            while True:
                self.oneround()
                if self.judgewinner(0) != -1:
                    return self.judgewinner(0)
                pass  # TODO
        elif self.wtype == 'round':
            while self.round != -1:
                self.oneround()
                if self.judgewinner(0) != -1:
                    return self.judgewinner(0)
                self.round -= 1

        return self.judgewinner(end=1)

    def judgewinner(self, end):
        if(end != 1):
            tmpCount = 0
            tmpPlayer = -1
            for i in range(0, self.psize):
                if(self.players[i].balance > 0):
                    tmpCount += 1
                    tmpPlayer = i
            if tmpCount == 1:
                return tmpPlayer
            else:
            	return -1
        else:
            maxBalance = 0
            richestPlayer = -1
            for i in range(0, self.psize):
                if self.players[i].balance > maxBalance:
                    maxBalance = self.players[i].balance
                    richestPlayer = i
            return richestPlayer

    def oneround(self):
        for i in range(0, self.psize):
            self.players[i].play()
            self.map.display()

if __name__ == '__main__':
    game = controller('small', 3, 'dead', 10)
    game.gamebegin()
