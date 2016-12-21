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
        self.owner = -1
        self.bname = bname

        self.trigger = None

    #################
    # toString      #
    #################

    def __str__(self):
        return '{6:<12}\t[{0}] ({1:<5},{2:<5})\tOwner:{3};\t next:{4},prev:{5}'.format(
            self.btype[0], self.bvalue, self.bincome, self.owner, self.bnext.bname,
            self.blast.bname, self.bname)


class district:

    #########################################################
    # Initialize                                            #
    # msize:    Map size = small OR medium OR huge OR crazy #
    # mseed:    Map generation seed                         #
    #########################################################

    def __init__(self, msize, mseed=1):
        self.msize = sizeTable[msize]
        self.mseed = mseed
        self.blocks = []
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
        for i in range(0, len(self.blocks)):
            self.blocks[i].blast = self.blocks[i - 1]
            self.blocks[i - 1].bnext = self.blocks[i]


    def display(self):
        for i in self.blocks:
            print(i)

sizeTable = {'small': 30, 'medium': 50, 'large': 100, 'crazy': 150}

blockname = ['北京', '上海', '广州','天津','重庆','石家庄','太原','西安','沈阳','长春','哈尔滨',\
        '济南','南京','杭州','福州','南宁','南昌','长沙','武汉','郑州','银川','西宁','兰州',\
        '拉萨','昆明','成都','贵阳','乌鲁木齐','呼和浩特','合肥','深圳','青岛','苏州','大连',\
        '宁波','无锡','厦门','常州','东莞','温州','佛山','海口','台北','湖州','唐山','临沂',\
        '嘉兴','绍兴','南通','徐州','泉州','烟台','潍坊','珠海','洛阳','中山','金华','淮安',\
        '威海','淄博','扬州','芜湖','盐城','宜昌','襄阳','绵阳','新竹','高雄','保定','延安',\
        '大同','大理','日喀则','喀什','桂林','齐齐哈尔','三亚','香港','澳门','新加坡','平壤','首尔','东京']

if __name__ == '__main__':
    m = district('medium')
    m.display()
