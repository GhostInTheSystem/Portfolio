number = int(input("Enter your number. Make sure it is whole and greater than zero."))
if (number < 1):
    print ("Please enter a number that is greater than zero")
elif (number % 1!= 0):
    print ("Please enter a whole number")
else:
    print (number)
    while (number != 1):
        if (number % 2 == 0):
            nrumber = (number / 2)
            print (number)
        else:
            number = ((number * 3) + 1)
            print (number)
