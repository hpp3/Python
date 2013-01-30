#register map class

import test as t
import collections as c


memory = c.defaultdict(int)

def showmemory(base):
    for i in memory:
        print base(memory[i])

class regmap:
    
    def __init__(self, regbase, regsize):
        self.base = regbase
        self.size = regsize

    def rd(self, name, args=[]):
        global memory
        if type(args) == int: args = [args]
        (flags,width,addr,size,default,string) = name(*args)
        addr += self.base
        value = 0
        i = 0
        while (size > 0):
            change = (width - addr%width)
            mask = (1 << size) - 1
            mask <<= addr % width
            word = memory[addr/width]
            value = value | (((word & mask) >> addr % width) << i)
            i += change
            addr += change
            size -= change
        return value

    
    def wr(self, value, name, args=[]):
        global memory
        if type(args) == int: args = [args]
        (flags,width,addr,size,default,string) = name(*args)
        addr += self.base
        mask = (1 << size) - 1
        value &= mask
        while (size > 0):
            change = (width - addr%width)
            mask = (1 << size) - 1
            mask <<= addr % width
            word = memory[addr/width]
            width_mask = (1 << change) - 1
            memory[addr/width] = (word & ~mask) | ((value & width_mask) << (addr % width))
            addr += change
            size -= change
            value >>= change

    def rh(self, name):
        print(hex(self.rd(name)))

    
a = regmap(regbase=0, regsize=4)

## USAGE:
## >>> a.wr(10, t.ONE)
## >>> a.rd(t.ONE)
## 10
## >>> a.wr(1000, t.THREE)
## >>> a.rd(t.THREE)
## 1000
## >>> a.wr(1, t.VAR, 0)
## >>> a.rd(t.VAR, 0)
## 1
## >>> a.wr(1, t.VAR, 1)
## >>> a.rd(t.VAR, 1)
## 1
## >>> showmemory(int)
## 71
## 31
## >>> showmemory(hex)
## 0x47
## 0x1f
## >>> showmemory(bin)
## 0b1000111
## 0b11111
