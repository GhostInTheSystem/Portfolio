num = int(input("How many places do you want to go to?"))
count = 1
while (count <= num):
    if ((count%3==0) and (count%5==0)):
        print ("Fizzbuzz")
    elif (count%3==0):
        print ("Fizz")
    elif (count%5==0):
        print ("Buzz")
    else:
        print (count)
    count += 1
