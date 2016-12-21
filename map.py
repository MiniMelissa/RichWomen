import random


class block:

    def __init__(self, btype, bvalue, bincome, bnext, blast, bname):
        self.btype = btype
        self.bvalue = bvalue
        self.bincome = bincome
        self.bnext = bnext
        self.blast = blast
        self.owner = -1
        self.bname = bname
        self.players = []

    def __str__(self):
        return 'Blocks:{0}, ({1},{2})\tOwner:{3};\t next:{4},prev:{5}'.format(
            self.btype, self.bvalue, self.bincome, self.owner, self.bnext.bname,
            self.blast.bname)


class district:

    def __init__(self, msize):
        self.msize = msize
        self.blocks = []
        self.players = []

        for i in range(0, sizeTable[self.msize]):
            tmpB = block('normal', random.randint(30, 60) * 10, random.randint(30, 60) * 1000,
                         None, None, i)
            self.blocks.append(tmpB)
        for i in range(0, len(self.blocks)):
            self.blocks[i].blast = self.blocks[i - 1]
            self.blocks[i - 1].bnext = self.blocks[i]
        self.msize = sizeTable[self.msize]

    def updatePlayerLocation(self, player, moveSteps):
    	for i in range(0, self.msize):
    		if player in self.blocks[i].players:
    			tmp = i
    			self.blocks[i].players.remove(player)

        for i in range(0, moveSteps):	#TODO: while loop
            tmp = tmp + 1

            if tmp >= self.msize:
            	tmp = tmp % self.msize

            if self.blocks[tmp].btype == 'bomb':
            	tmp = 0	#TODO: hospital loc
                break

        location = tmp
        self.blocks[location].players.append(player)
        return location

    def display(self):
        for i in self.blocks:
            print(i)

sizeTable = {'small': 10, 'medium': 20, 'large': 30, 'crazy': 150}

# if __name__ == '__main__':
#     m = district('small')
#     m.display()
