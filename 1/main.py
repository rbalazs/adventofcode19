import os
import math
filepath = os.path.dirname(os.path.realpath(__file__)) + '/input'

module = []
sum = 0

def calc(mass):
    mass = int(math.floor(mass/3)-2)
    if mass < 0:
        return 0
    return mass


with open(filepath) as fp:
   line = fp.readline()
   while line:
       mass = int(line)
       c = 0
       while mass > 0 and c < 1000:
            c = c+1
            mass = calc(mass)
            sum = sum + mass


       line = fp.readline()



print(sum)
