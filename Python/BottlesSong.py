bottle = int(input("How many bottles do you have? Make sure it is whole and greater than zero."))
if (bottle < 1):
    print ("Please enter a number that is greater than zero")
elif (bottle % 1!= 0):
    print ("Please enter a whole number")
else:
    while (bottle > 0):
        if (bottle > 2):
            print (bottle , " bottles of hard whiskey on the wall, " , bottle , " bottles of hard whiskey! You take one down, pass it around, " , bottle-1 , " bottles of hard whiskey on the wall!")
            bottle -= 1
        elif (bottle == 2):
            print (bottle , " bottles of hard whiskey on the wall, " , bottle , " bottles of hard whiskey! You take one down, pass it around, " , bottle-1 , " bottle of hard whiskey on the wall!")
            bottle -= 1
        else:
            print (bottle , " bottle of hard whiskey on the wall, " , bottle , " bottle of hard whiskey! You take one down, pass it around, " , bottle-1 , " bottles of hard whiskey on the wall!")
            bottle -= 1
