import random
diceType, diceNum, diceMod = int(input("Please enter the number of sides on the dice.")), int(input("Please enter the number of dice.")), int(input("Please enter the modifier."))
def rollDice(sides, num, mod):
    if (not((sides>=1)|(sides%1==0)|(num>=1)|(num%1==0)|(mod%1==0))):
        print ("Invalid")
    else:
        dice1 = list(range(1, sides+1, 1))
        total = 0
        while (num > 0):
            roll = dice1[random.randrange(0, sides, 1)]
            print (roll)
            total += roll
            num -= 1
        total += mod
        print ("Your total is: " , total)
rollDice(diceType, diceNum, diceMod)
