# -*- coding: UTF-8 -*-
import random


class block:

    #################################################################
    # Initialize                                                    #
    # btype:    block type = 'normal' OR 'super' OR 'jail'(TODO)    #
    # bvalue:   block value                                         #
    # bincome:  block income                                        #
    # bnext:    next block                                          #
    # blast:    last block                                          #
    # bname:    block name                                          #        
    #################################################################

    def __init__(self, btype, bvalue, bincome, bnext, blast, bname):
        self.btype = btype
        self.bvalue = bvalue
        self.bincome = bincome
        self.bnext = bnext
        self.blast = blast
        self.owner = 'Tom'
        self.bname = bname
        self.players = []
        self.level = 0


        self.trigger = None
        self.display_type = 0

    #################
    # toString      #
    #################

    def __str__(self):
        if self.display_type == 0:
            return '{6:<12}\t[{0}] ({1:<5},{2:<5})\tOwner:{3};\t next:{4},prev:{5}'.format(
                self.btype[0], self.bvalue, self.bincome, self.owner, self.bnext.bname, self.blast.bname, self.bname)
        else:
            # Size: 24 * 2  
            # #-----------------------#
            # | Name________ Owner_   |
            # | [T] Lv.3  99999/99999 |
            # #-----------------------#
            return ' {0:<12}  {1:>8} \n [{2:1}] {3:3}{4:<2}  {5:<5}{6}{7:>5} '.format(
                    self.bname,\
                    self.owner if self.bvalue!=-1 else '',\
                    self.btype[0].upper(),\
                    'Lv.' if self.bvalue!=-1 else '   ',\
                    self.level if self.bvalue!=-1 else '',\
                    self.bvalue if self.bvalue!=-1 else '',\
                    '/' if self.bvalue!=-1 else ' ',\
                    self.bincome if self.bvalue!=-1 else '')
class district: 

    #########################################################
    # Initialize                                            #
    # msize:    Map size = small OR medium OR huge OR crazy #
    # mseed:    Map generation seed                         #
    #########################################################

    def __init__(self, msize, mseed=1):
        
        # Basic Variables
        self.msize = sizeTable[msize]
        self.blocks = []

        # Mid-Level Variables
        self.mseed = mseed

        self.hospital_loc = -1
        self.jail_loc = -1
        

        # Preparation Method 
        self.generate_map()

    #########################################
    # generate a new map                    #
    # TODO: adding different types of map   #
    #########################################

    def generate_map(self):
        
        # configuration
        value_base = 30
        value_head = 60
        income_base = 30
        income_head = 60
        multiple = 10
        sumper_multiple = 5

        # Add blocks
        prevalue = -1
        preincome = -1

        namepool = blockname[:]
        
        # Generate normal and super blocks
        for i in range(0, self.msize):

            # super blocks
            if random.randint(1, 100) >=80 :
                name = blockname.pop(random.randint(0, len(blockname)-1))
                value = random.randint(value_base, value_head) * multiple * sumper_multiple
                income = random.randint(income_base, income_head) * multiple * sumper_multiple 
                tmpB = block('super', value, income, None, None, name)
                prevalue = preincome = -1

            # normal blocks
            else: 
                name = blockname.pop(random.randint(0, len(blockname)-1))
                if prevalue == -1:
                    value = random.randint(value_base, value_head) * multiple
                    income = random.randint(income_base, income_head) * multiple 
                    tmpB = block('normal', value, income, None, None, name)
                    prevalue = value 
                    preincome = income
                else:
                    if random.randint(0, 10) >= 8:
                        value = random.randint(value_base, value_head) * multiple
                        income = random.randint(income_base, income_head) * multiple 
                        tmpB = block('normal', value, income, None, None, name)
                        prevalue = value 
                        preincome = income
                    else:
                        tmpB = block('normal', prevalue, preincome, None, None, name)

            self.blocks.append(tmpB)

        # Genertae Only-one Special blocks
        # Hospital:
        self.hospital_loc = random.randint(0, self.msize-1)
        self.blocks[self.hospital_loc] = block('hospital', -1, -1, None, None, 'Hospital')
        # Jail
        skew_value = random.randint(-5, 5)
        self.jail_loc = (self.hospital_loc + self.msize/2) % self.msize + skew_value
        self.blocks[self.jail_loc] = block('jail', -1, -1, None, None, 'Jail')
        
        for i in range(0, len(self.blocks)):
            self.blocks[i].blast = self.blocks[i - 1]
            self.blocks[i - 1].bnext = self.blocks[i]


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
            	tmp = self.hospital_loc
                break

        location = tmp
        self.blocks[location].players.append(player)
        return location

    def display(self):
        for i in self.blocks:
            i.display_type = 1
            print '------------------------'
            print(i)

sizeTable = {'small': 30, 'medium': 50, 'large': 100, 'crazy': 150}

blockname = ['北京', '上海', '广州','天津','重庆','石家庄','太原','西安','沈阳','长春','哈尔滨',\
        '济南','南京','杭州','福州','南宁','南昌','长沙','武汉','郑州','银川','西宁','兰州',\
        '拉萨','昆明','成都','贵阳','乌鲁木齐','呼和浩特','合肥','深圳','青岛','苏州','大连',\
        '宁波','无锡','厦门','常州','东莞','温州','佛山','海口','台北','湖州','唐山','临沂',\
        '嘉兴','绍兴','南通','徐州','泉州','烟台','潍坊','珠海','洛阳','中山','金华','淮安',\
        '威海','淄博','扬州','芜湖','盐城','宜昌','襄阳','绵阳','新竹','高雄','保定','延安',\
        '大同','大理','日喀则','喀什','桂林','齐齐哈尔','三亚','香港','澳门','Singapore','平壤','Seoul','Tokyo']

if __name__ == '__main__':
    m = district('small')
    m.display()
