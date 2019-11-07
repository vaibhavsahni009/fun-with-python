from random import randint
from face import diceface

def roll():
    return diceface(randint(1,6))

x='y'

while(x=='y'):
    roll()
    x=input("Enter y to roll again ")
