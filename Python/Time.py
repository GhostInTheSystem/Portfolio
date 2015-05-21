import datetime;

now = datetime.datetime.now()
userInput = input("Please enter your birthday in YYY/MM/DD format")
if (len(userInput) == 10):
    userDay = userInput[8:10]
    userMonth = userInput[5:7]
    userYear = userInput[0:4]
    dage = now.day - int(userDay)
    mage = now.month - int(userMonth)
    yage = now.year - int(userYear)
    timeDif = (yage * 365 + mage * 30.4 + dage)
    endYage = int(timeDif/365)
    endMage = int((timeDif - endYage*365)-((timeDif - endYage*365)%30.4))/30.4
    endDage = int(timeDif - endYage*365 - endMage*30.4)
    print("You are " , endYage , " years, " , endMage ,  " months and " , endDage , "days old")
else :
    print ("Your input is wrong. Try again.")
